from subprocess import check_output, call
import os

def test_simple():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "simple"
    assert "TEST_SIMPLE\n" == check_output(["./ssh-restrict", "./test/config"])

def test_args():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "args 23 42"
    assert "23 42\n" == check_output(["./ssh-restrict", "./test/config"])

def test_undefined():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "undefined"
    assert call(["./ssh-restrict", "./test/config"]) == 1

def test_notfound():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "notfound"
    assert call(["./ssh-restrict", "./test/config"]) == 127
