# coding: windows-1252
# Using windows-1252 as utf-8 did not work for character '±'
#
# Unit tests to validate the regular expression in module app.postcode against given test data.
#
# Author: Matthew Golab
# Date: 30/5/17

import unittest
import app

from app.postcode import Postcode

import app.postcode

# Test data:             #Postcode:     Expected result    Test Case scenario:                              Expected problem:
#                                       (regex matches):    
UnitTestPostcodeData = [ ["$%± ()()",   False,            "Junk"                                        ],   # Junk
                         ["XX XXX",     False,            "Invalid"                                     ],  # Invalid
                         ["A1 9A",      False,            "Incorrect inward code length"                ],  # Incorrect inward code length
                         ["LS44PL",     False,            "No space"                                    ],  # No space
                         ["Q1A 9AA",    False,            "'Q' in first position"                       ],  # 'Q' in first position
                         ["V1A 9AA",    False,            "'V' in first position"                       ],  # 'V' in first position
                         ["X1A 9BB",    False,            "'X' in first position"                       ],  # 'X' in first position
                         ["LI10 3QP",   False,            "'I' in second position"                      ],  # 'I' in second position
                         ["LJ10 3QP",   False,            "'J' in second position"                      ],  # 'J' in second position
                         ["LZ10 3QP",   False,            "'Z' in second position"                      ],  # 'Z' in second position
                         ["A9Q 9AA",    False,            "'Q' in third position with 'A9A' structure"  ],  # 'Q' in third position with 'A9A' structure
                         ["AA9C 9AA",   False,            "'C' in fourth position with 'AA9A' structure"],  # 'C' in fourth position with 'AA9A' structure
                         ["FY10 4PL",   False,            "Area with only single digit districts"       ],  # Area with only single digit districts
                         ["SO1 4QQ",    False,            "Area with only double digit districts"       ],  # Area with only double digit districts
                         ["EC1A 1BB",   True,             "None - valid postcode"                       ],  # None
                         ["W1A 0AX",    True,             "None - valid postcode"                       ],  # None
                         ["M1 1AE",     True,             "None - valid postcode"                       ],  # None
                         ["B33 8TH",    True,             "None - valid postcode"                       ],  # None
                         ["CR2 6XH",    True,             "None - valid postcode"                       ],  # None
                         ["DN55 1PT",   True,             "None - valid postcode"                       ],  # None
                         ["GIR 0AA",    True,             "None - valid postcode"                       ],  # None
                         ["SO10 9AA",   True,             "None - valid postcode"                       ],  # None
                         ["FY9 9AA",    True,             "None - valid postcode"                       ],  # None
                         ["WC1A 9AA",   True,             "None - valid postcode"                       ] ]  # None

# Define unit tests:
class TestPostCodeRegEx(unittest.TestCase):
    def setUp (self):
        self.postcode = Postcode(app.postcode.regular_expression)

    def test_junk_postcode (self):
        expectedResult = UnitTestPostcodeData[0][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[0][0])
        self.assertEqual(result,expectedResult)

    def test_invalid_postcode (self):
        expectedResult = UnitTestPostcodeData[1][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[1][0])
        self.assertEqual(result,expectedResult)

    def test_incorrect_inward_code_length (self):
        expectedResult = UnitTestPostcodeData[2][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[2][0])
        self.assertEqual(result,expectedResult)
    def test_no_space (self):
        expectedResult = UnitTestPostcodeData[3][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[3][0])
        self.assertEqual(result,expectedResult)

    def test_q_in_first_position (self):
        expectedResult = UnitTestPostcodeData[4][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[4][0])
        self.assertEqual(result,expectedResult)

    def test_v_in_first_position (self):
        expectedResult = UnitTestPostcodeData[5][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[5][0])
        self.assertEqual(result,expectedResult)

    def test_x_in_first_position (self):
        expectedResult = UnitTestPostcodeData[6][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[6][0])
        self.assertEqual(result,expectedResult)

    def test_i_in_first_position (self):
        expectedResult = UnitTestPostcodeData[7][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[7][0])
        self.assertEqual(result,expectedResult)

    def test_j_in_first_position (self):
        expectedResult = UnitTestPostcodeData[8][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[8][0])
        self.assertEqual(result,expectedResult)

    def test_z_in_first_position (self):
        expectedResult = UnitTestPostcodeData[9][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[9][0])
        self.assertEqual(result,expectedResult)

    def test_q_in_first_position (self):
        expectedResult = UnitTestPostcodeData[10][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[10][0])
        self.assertEqual(result,expectedResult)

    def test_c_in_first_position (self):
        expectedResult = UnitTestPostcodeData[11][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[11][0])
        self.assertEqual(result,expectedResult)

    def test_area_with_single_digit_districts (self):
        expectedResult = UnitTestPostcodeData[12][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[12][0])
        self.assertEqual(result,expectedResult)

    def test_area_with_double_digit_districts (self):
        expectedResult = UnitTestPostcodeData[13][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[13][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode1 (self):
        expectedResult = UnitTestPostcodeData[14][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[14][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode2 (self):
        expectedResult = UnitTestPostcodeData[15][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[15][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode3 (self):
        expectedResult = UnitTestPostcodeData[16][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[16][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode4 (self):
        expectedResult = UnitTestPostcodeData[17][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[17][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode5 (self):
        expectedResult = UnitTestPostcodeData[18][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[18][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode6 (self):
        expectedResult = UnitTestPostcodeData[19][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[19][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode7 (self):
        expectedResult = UnitTestPostcodeData[20][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[20][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode8 (self):
        expectedResult = UnitTestPostcodeData[21][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[21][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode9 (self):
        expectedResult = UnitTestPostcodeData[22][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[22][0])
        self.assertEqual(result,expectedResult)

    def test_valid_postcode10 (self):
        expectedResult = UnitTestPostcodeData[23][1]
        result = self.postcode.TestPostCode(UnitTestPostcodeData[23][0])
        self.assertEqual(result,expectedResult)

if __name__ == '__main__':
    unittest.main()
