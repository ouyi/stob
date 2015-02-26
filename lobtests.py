#!/usr/bin/env python
from lob import * 
import unittest

class LobTests(unittest.TestCase):

    def test_randstr(self):
        self.failUnless( 10 == len(randstr(10)) )

    def test_obfuscate_one_elem(self):
        s = ["abcdefg"]
        o = obfuscate(s)
        self.failUnless( len(s) == len(o) )

    def test_obfuscate_multi_elem(self):
        s = ["abcdefg", "opq"]

        o = obfuscate(s)
        self.failUnless( len(s) == len(o) )
        self.failUnless( s != o )

        o = obfuscate(s, [0])
        self.failUnless( len(s) == len(o) )
        self.failUnless( s != o )

        o = obfuscate(s, [1])
        self.failUnless( len(s) == len(o) )
        self.failUnless( s != o )

def main():
    unittest.main()

if __name__ == '__main__':
    main()
