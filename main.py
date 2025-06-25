import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    content = " ".join(sys.argv)
    if len(sys.argv) < 2:
        sys.exit(1)

    model = "gemini-2.0-flash-001"

    response = response = client.models.generate_content(model=model, contents=content)


    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(f"response {response.text}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()