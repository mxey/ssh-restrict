from subprocess import check_output, call
import os

EXPECTED_RETURN_CODE_WRONG_USAGE = 3
EXPECTED_RETURN_CODE_COMMAND_NOT_FOUND = 3

def test_simple():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "simple"
    assert "TEST_SIMPLE\n" == check_output(["./ssh-restrict", "./test/config"])

def test_args():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "args 23 42"
    assert "23 42\n" == check_output(["./ssh-restrict", "./test/config"])

def test_undefined():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "undefined"
    assert call(["./ssh-restrict", "./test/config"]) == EXPECTED_RETURN_CODE_COMMAND_NOT_FOUND

def test_notfound():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "notfound"
    assert call(["./ssh-restrict", "./test/config"]) == EXPECTED_RETURN_CODE_WRONG_USAGE
