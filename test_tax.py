# -*- coding: utf-8 -*-
import tax
import unittest

class taxTestCase(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(tax.tax(30000, 20, 1), "나이 : 20, 내야하는 세금 : 13500")
   
    def test_tax_abnormal(self):
        self.assertEqual(tax.tax(30000, 20, 1), "나이 : 20, 내야하는 세금 : 15000")

if __name__ == "__main__":
    unittest.main(verbosity=2)

