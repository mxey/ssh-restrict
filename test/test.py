import unittest
from subprocess import check_output, call
import os

class SSHRestrictTestCase(unittest.TestCase):
    def test_simple(self):
        os.environ["SSH_ORIGINAL_COMMAND"] =  "simple"
        self.assertEqual(
            "TEST_SIMPLE\n",
            check_output(["./ssh-restrict", "./test/config"])
        )

    def test_args(self):
        os.environ["SSH_ORIGINAL_COMMAND"] =  "args 23 42"
        self.assertEqual(
            "23 42\n", 
            check_output(["./ssh-restrict", "./test/config"])
        )

    def test_undefined(self):
        os.environ["SSH_ORIGINAL_COMMAND"] =  "undefined"
        self.assertEqual(
            call(["./ssh-restrict", "./test/config"]),
            1
        )

    def test_notfound(self):
        os.environ["SSH_ORIGINAL_COMMAND"] =  "notfound"
        self.assertEqual(
            call(["./ssh-restrict", "./test/config"]),
            127
        )

if __name__ == '__main__':
    unittest.main()
