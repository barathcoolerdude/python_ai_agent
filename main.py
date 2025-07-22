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
from call_function import *
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
    messages = []
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    

    # Function to handle Gemini generation and response
    iters = 0

    while True:
        iters += 1
        print(f"\n iteration {iters} of 5\n")
        if iters > 5:
            print(f"Maximum iterations (5) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

def generate_content(client, messages, verbose):
    # Generate content using the client
    model = "gemini-2.0-flash-001"
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    response = client.models.generate_content(model=model, contents=messages, config =config, )
    # if text is empty, print metadata
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    for candidate in response.candidates:
        messages.append(candidate.content)
    if not response.function_calls:
        return response.text
    
    # check to see if agent wants to call a function
    function_response = []
    for function_call_part in response.function_calls:
        call_function_result = call_function(function_call_part, verbose)      
        if not call_function_result.parts[0]:
            raise Exception("a fatal exception of some sort.")
        if verbose:
            print(f"\nfunction call response -> {call_function_result.parts[0]}")

        function_response.append(call_function_result.parts[0])

    if not function_response:
        raise Exception("\n No function response generated.\n")
    
    messages.append(types.Content(parts = function_response,role="tool",))
    

if __name__ == "__main__":
    main()