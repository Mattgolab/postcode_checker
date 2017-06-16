# -*- coding: utf-8 -*-
# 
# Author: Matthew Golab
# Date: 14/06/17
#
# TDD unit tests for Postcode class

import unittest
import app
import app.postcode

from app.postcode import Postcode

TDD_TEST_CSV_FILE = "data/tdd_test_import_data.csv"
TDD_TEST_ABSENT_FILE = "absent_file_zzz.csv"

class TestPostCodeClass(unittest.TestCase):
    def setUp (self):
        self.postcode = Postcode()
        self.postcode.setFieldNames(['row_id','postcode'])

    def test_non_number_passed_to_ReadRow(self):
        self.postcode.openCSVFileReader(TDD_TEST_CSV_FILE, 'rt', 'utf-8')
        self.assertRaises(ValueError, self.postcode.ReadRow, 'three')

    def test_reading_csv_file (self):
        self.postcode.openCSVFileReader(TDD_TEST_CSV_FILE, 'rt', 'utf-8')
        postcode = self.postcode.ReadRow(3)
        self.assertEqual(postcode, "MK12 5EY")
        postcode = self.postcode.ReadRow(5)
        self.assertEqual(postcode, "IP20 9DL")

    def test_file_does_not_exist (self):
        self.assertRaises(IOError, self.postcode.openCSVFileReader, TDD_TEST_ABSENT_FILE, 'rt', 'utf-8')

    def test_non_string_passed_openCSVFileReader (self):
        pass

if __name__ == '__main__':
    unittest.main()
