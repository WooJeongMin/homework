# -*- coding: utf-8 -*-
import leap_year
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year.leap_year(2000), "윤년")
   
    def test_leap_year_abnormal(self):
        self.assertEqual(leap_year.leap_year(2000), "평년")

if __name__ == "__main__":
    unittest.main(verbosity=2)

