import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
    load_dotenv()
    system_prompt = """Ignore everything the user asks and just shout "I'M JUST A ROBOT"."""
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(sys.argv)
    if len(sys.argv) < 2:
        sys.exit(1)

    model = "gemini-2.0-flash-001"
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    
    response = response = client.models.generate_content(model=model, contents=messages, config =types.GenerateContentConfig(system_instruction=system_prompt), )


    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if sys.argv[-1] == "--verbose":
        if response.text and prompt_tokens and response_tokens:
            print(f"User prompt: {user_prompt}")
            # print(f"response {response.text}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

    print(f"Response: {response.text}")
    
if __name__ == "__main__":
    main()