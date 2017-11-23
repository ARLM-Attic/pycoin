import unittest
import hashlib

from pycoin.contrib.ripemd import new as ripemd160
from pycoin.contrib.ripemd import test_ripemd as selftest

class RipemdTest(unittest.TestCase):
    def test_ripemd_knowns(self):
        selftest()

    def test_ripemd_vs_stdlib(self):
        try:
            hashlib.new('ripemd160')
        except:
            # GAE and micropython may not have native code
            return

        for msg in (b'', b'abc', b'sdfdlfjskljsdfjfkldsjklfdsjkfldsljkdfs'):
            lib = hashlib.new('ripemd160', msg)
            assert ripemd160(msg).digest() == lib.digest()

if __name__ == '__main__':
    unittest.main()
