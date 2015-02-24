#!/usr/bin/python
import os
import sys
sys.path.append('../lib/deid/')
import nose
from deid import deid

def test_deid():
    cwd = os.getcwd()
    assert deid(cwd+"/test_data")==0
if __name__ == '__main__':
        nose.runmodule()
