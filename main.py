import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import *
from prompt import system_prompt
def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if len(sys.argv) < 2:
        sys.exit(1)

    model = "gemini-2.0-flash-001"
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    response = client.models.generate_content(model=model, contents=messages, config =config, )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count


    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if response.function_calls:

        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    else:
        print("💬 Text response:", response.text)


if __name__ == "__main__":
    main()