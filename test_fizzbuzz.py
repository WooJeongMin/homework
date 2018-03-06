# -*- coding: utf-8 -*-
import fizzbuzz
import unittest

class fizzbuzzTestCase(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), ['ValueError', 1, 2, 'fizz', 4, 'buzz'])
    def test_fizzbuzz_abnormal(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), ['ValueError', 1, 2, 'fizz', 4, ])

if __name__ == "__main__":
    unittest.main(verbosity=2)
