from server import process_client_message
import unittest
from lesson4.common.variables import *


class TestServer(unittest.TestCase):

    ok_dict = {RESPONSE: 200}
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_ok_check(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1}), self.err_dict)

    def test_unknown_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'user'}}), self.err_dict)

    def test_no_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1}), self.err_dict)

    def test_wrong_action(self):
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()
