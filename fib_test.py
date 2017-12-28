#!/usr/bin/env python3
import unittest
from fib import fib

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib._fib(37), 24157817)


if __name__ == '__main__':
    unittest.main()
