from subprocess import check_output, call
import os

# Expected return codes
return_code_unknown = 3
return_code_notfound = return_code_unknown

def test_simple():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "simple"
    assert b"TEST_SIMPLE\n" == check_output(["./ssh-restrict", "./test/config"])

def test_args():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "args 23 42"
    assert b"23 42\n" == check_output(["./ssh-restrict", "./test/config"])

def test_undefined():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "undefined"
    assert call(["./ssh-restrict", "./test/config"]) == return_code_unknown

def test_notfound():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "notfound"
    assert call(["./ssh-restrict", "./test/config"]) == return_code_notfound

def test_fail_def():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "fail_def test"
    assert call(["./ssh-restrict", "./test/config"]) == return_code_unknown

def test_fail_com():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "fail_com 123"
    assert call(["./ssh-restrict", "./test/config"]) == return_code_unknown

def test_fail_eval():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "print_int notint"
    assert call(["./ssh-restrict", "./test/config"]) == return_code_unknown

def test_match():
    os.environ["SSH_ORIGINAL_COMMAND"] =  "match"
    assert b"match2\n" == check_output(["./ssh-restrict", "./test/config"])
