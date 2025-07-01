import os
import unittest
from calculator.functions.get_files_info import *

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print(f"result0: {result}")

    def test_get_files_info_1(self):
        result = get_files_info("calculator", "pkg")
        print(f"result1: {result}")

    def test_get_files_info_2(self):
        result = get_files_info("calculator", "/bin")
        print(f"result2: {result}")

    def test_get_files_info_3(self):
        result = get_files_info("calculator", "../")
        print(f"result3: {result}")

if __name__ == '__main__':
    unittest.main()
        