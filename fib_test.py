#!/usr/bin/env python3
import unittest
from fib import fib_standard, fib_rec_memo

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib_standard(37), 24157817)

    def test2(self):
        self.assertEqual(fib_rec_memo(10), 89)

if __name__ == '__main__':
    unittest.main()
