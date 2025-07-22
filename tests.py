import os
import unittest
from functions.get_files_info import *
from functions.run_python import *
from main import *

from dotenv import load_dotenv

#imprt google genai client and types
from google import genai
from google.genai import types

class TestGetFilesInfo(unittest.TestCase):
    # def test_get_files_info(self):
    #     result = get_files_info("calculator", ".")
    #     print(f"result0: {result}")

    # def test_get_files_info_1(self):
    #     result = get_files_info("calculator", "pkg")
    #     print(f"result1: {result}")

    # def test_get_files_info_2(self):
    #     result = get_files_info("calculator", "/bin")
    #     print(f"result2: {result}")

    # def test_get_files_info_3(self):
    #     result = get_files_info("calculator", "../")
    #     print(f"result3: {result}")

    # def test_get_file_content(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     self.assertGreater(len(result), 10000)
    #     self.assertLess(len(result), 10100)
    #     self.assertTrue(result.endswith('[...File "lorem.txt" truncated at 10000 characters]'))

    # def test_get_file_content_2(self):
    #     result = get_file_content("calculator", "main.py")
    #     print(f"result4: {result}")
    #     with open("calculator/main.py", 'r') as file:
    #         content = file.read()
    #     self.assertEqual(result, content)

    # def test_get_file_content_3(self):
    #     result = get_file_content("calculator", "pkg/calculator.py")
    #     print(f"result5: {result}")
    #     with open("calculator/pkg/calculator.py", 'r') as file:
    #         content = file.read()
    #     self.assertEqual(result, content)

    # def test_get_file_content_4(self):
    #     result = get_file_content("calculator", "/bin/cat")
    #     print(f"result6: {result}")
    #     self.assertEqual(result, 'Error: Cannot list "/bin/cat" as it is outside the permitted working directory')

    # def test_get_file_content_write_file(self):
    #     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     length = len("wait, this isn't lorem ipsum")
    #     print(f'result: {result}')
    #     self.assertEqual(result, f'Successfully wrote to "lorem.txt" ({length} characters written)')        

    # def test_get_file_content_write_file_2(self):
    #     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #     length = len("lorem ipsum dolor sit amet")
    #     print(f'result: {result}')
    #     self.assertEqual(result, f'Successfully wrote to "pkg/morelorem.txt" ({length} characters written)')  

    # def test_get_file_content_write_file_3(self):
    #     result =   write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #     print(f'result: {result}')
    #     self.assertEqual(result, f'Error: Cannot list "/tmp/temp.txt" as it is outside the permitted working directory')

    def test_run_python_file(self):
        result = run_python_file("calculator", "main.py")
        print(f"result: {result}")
        
    def test_run_python_file_2(self):
        result = run_python_file("calculator", "tests.py")
        print(f"result2: {result}")

    def test_run_python_file_3(self):
        result = run_python_file("calculator", "../main.py")
        print(f"result3: {result}")

    def test_run_python_file_4(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(f"result4: {result}")

    # Load environment variables from .env file
    # load_dotenv()
    # def test_generate_content_full_messages(self):
    #     api_key = os.environ.get("GEMINI_API_KEY")
    #     client = genai.Client(api_key=api_key)
    #     messages = ["hi", "hello"]
    #     for i in messages:
    #         full_messages = generate_content(client, i, verbose = True)
    #     print(f"test full_messages: {full_messages}")


    

if __name__ == '__main__':
    unittest.main()
        