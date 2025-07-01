import os
import unittest
from get_files_info import *

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        os.mkdir('src')
        with open('readme.md', 'w') as f:
            f.write('This is a test file.')
        with open("package.json", 'w') as f:
            f.write('{"name": "joe", "age": "40"}')

    def tearDown(self):
        os.remove('readme.md')
        os.rmdir('src')
        os.remove('package.json')

    def test_get_files_info_not_directory(self):
        result = get_files_info("/home/coolerdude/workspace/python_ai_agent/functions", "not_a_directory")
        self.assertEqual(result, 'Error: "not_a_directory" is not a directory')

    def test_get_files_info_not_directory(self):
        result = get_files_info("/home/coolerdude/workspace/python_ai_agent/functions", "/home/coolerdude/workspace/python_ai_agent/functions/src")
        self.assertEqual(result, "True")

    def test_get_files_info_outside_working_directory(self):
        result = get_files_info("/home/coolerdude/workspace/python_ai_agent/functions", "/home/coolerdude/workspace")
        self.assertEqual(result, 'Error: Cannot list "/home/coolerdude/workspace" as it is outside the permitted working directory')

if __name__ == '__main__':
    unittest.main()