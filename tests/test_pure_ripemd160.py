import unittest
import hashlib

from pycoin.contrib.ripemd import new as ripemd160
from pycoin.contrib.ripemd import test_ripemd as selftest

def test_ripemd_knowns():
    selftest()

def test_ripemd_vs_stdlib():
    try:
        hashlib.new('ripemd160')
    except ValueError:
        # GAE and micropython may not have it native
        return

    for msg in ('', 'abc', 'sdfdlfjskljsdfjfkldsjklfdsjkfldsljkdfs'):
        lib = hashlib.new('ripemd160', msg)
        assert ripemd160(msg).digest() == lib.digest()

