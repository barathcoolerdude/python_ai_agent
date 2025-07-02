import os
import unittest
from functions.get_files_info import *

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

    def test_get_file_content_2(self):
        result = get_file_content("calculator", "main.py")
        # print(f"result4: {result}")
        with open("calculator/main.py", 'r') as file:
            content = file.read()
        self.assertEqual(result, content)

    def test_get_file_content_3(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        # print(f"result5: {result}")
        with open("calculator/pkg/calculator.py", 'r') as file:
            content = file.read()
        self.assertEqual(result, content)

    def test_get_file_content_4(self):
        result = get_file_content("calculator", "/bin/cat")
        # print(f"result6: {result}")
        self.assertEqual(result, 'Error: Cannot list "/bin/cat" as it is outside the permitted working directory')
            

if __name__ == '__main__':
    unittest.main()
        