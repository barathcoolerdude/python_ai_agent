#import std lib
import os
import sys

#load environment variablse from .env file
from dotenv import load_dotenv

#imprt google genai client and types
from google import genai
from google.genai import types

# import available functions and system prompt
from functions.get_files_info import *
from functions.run_python import *
from prompt import system_prompt

def main():
    # Load environment variables from .env file
    load_dotenv()

    #check verbose flag
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    # if no argument is given gelp the user
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
    
    # import api key and create client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    #Build the message list to send to Gemini
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

    # Function to handle Gemini generation and response
    function_calls = generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    model = "gemini-2.0-flash-001"
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    # Generate content using the client
    response = client.models.generate_content(model=model, contents=messages, config =config, )

    # get token usage metadata
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # if text is empty, print metadata
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    function_call_parts = response.function_calls
    print(f"function_call_parts: {function_call_parts}")


    # check to see if agent wants to call a function
    if function_call_parts:

        for function_call_part in function_call_parts:
            function_call_result = call_function(function_call_part, verbose)

            if not function_call_result:
                raise Exception("a fatal exception of some sort.")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            return function_call_result

    else:
        print("💬 Text response:", response.text)

    return function_call_parts

        # calling the function
def call_function(function_calls, verbose=False):

    #check to see if user is runing a verbose mode
    if verbose:
        print(f"Calling function: name = {function_calls.name} args = ({function_calls.args})")
    else:
        print(f" -> Calling function name:  = {function_calls.name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_name = function_calls.name

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
                )
                ],
            )

    function_calls.args["working_directory"] = "./calculator"

    function_result= function_map[function_name](**function_calls.args)
    print(f"\n\n\nfunction_result: {function_result}")

    type_content = types.Content(
        role = "tool",
        parts=[
            types.Part.from_function_response(
                name = function_name,
                response = {"result": function_result},
            )
        ],
    )    
    print(f"\n type_content: {type_content.parts[0].function_response.response['result']}")

    return type_content

        



if __name__ == "__main__":
    main()