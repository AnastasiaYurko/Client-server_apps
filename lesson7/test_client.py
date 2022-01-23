import sys
import os
from client import process_ans, create_presence
import unittest
from lesson4.common.variables import *

RESPONSE_GOOD = {RESPONSE: 200}
PORT = DEFAULT_PORT
MESSAGE_GOOD = '200 : OK'

RESPONSE_BAD = {ERROR: 'Bad Request'}
EXPECTED_EXCEPTION = ValueError


class TestClass(unittest.TestCase):

    def test_def_presence(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_answer(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_answer_good(self):
        """Вариант предыдущего теста с переменными"""
        self.assertEqual(process_ans(RESPONSE_GOOD), MESSAGE_GOOD)

    def test_process_answer_error(self):
        """Исключение без поля RESPONSE"""
        self.assertRaises(EXPECTED_EXCEPTION, process_ans, RESPONSE_BAD)


if __name__ == '__main__':
    unittest.main()
