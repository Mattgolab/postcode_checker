# -*- coding: utf-8 -*-
# 12/05/17 Task: Implement Python script which validates the effectiveness of a given
#                regular expression.
# 
# Author: Matthew Golab
# 
# Part 1 - Postcode validation, create unit tests.
# Part 2 - Bulk import CSV file containing postcode data, check each postcode for
#          validity and output bad postcodes to CSV file named "failed_validation.csv"

# Imports
import re
import unittest
import csv
import sys

# Default regular expression used to validate UK postcodes:
regular_expression = r"""(GIR\s0AA) | 
                           (    
                                # A9 or A99 prefix
                                ( ([A-PR-UWYZ][0-9][0-9]?) |
                                    # AA99 prefix with some excluded areas
                                    (
                                        ([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
                                        # AA9 prefix with some excluded areas
                                        ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
                                        # WC1A prefix
                                        (WC[0-9][A-Z]) |
                                        (
                                            # A9A prefix
                                            ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                                            # AA9A prefix
                                            ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
                                        )
                                    )
                                )
                                # 9AA suffix
                                \s[0-9][ABD-HJLNP-UW-Z]{2}
                            )"""


class Postcode(object):
    def __init__(self):
        self.files = []

    def __del__(self):
        # Close any open files:
        for file in self.files:
            file.close()

    def loadRegex(self, regex_in):
        # For optimisation compile in given regex and pass in using raw string notation (instead of string literal) with 'r'.
        self.regex = re.compile(regex_in, re.X)

    # Validates a postcode passed in as a parameter, returns True if OK, else False.
    # pre-requisite: Load required Regex using method loadRegex()
    def testPostCode(self, postcode):
        if not re.fullmatch(self.regex, postcode):
            return False
        else:
            return True

    # Opens a CVS file and returns a csv.reader (dict) object:
    # example params: (<INPUT_CSV_FILE>, 'rt', 'utf-8')
    def openCSVFileReader(self, filename, rw_attribute, encoding):
        if isinstance(filename, str) and isinstance(rw_attribute, str) and isinstance(encoding, str):
            try:
                self.files.insert(0, open(filename, rw_attribute, encoding=encoding) )
                self.fileRead = self.files[0]
            except IOError:
                print("Error opening file %s"% filename)
                raise IOError
            self.csvReader = csv.DictReader(self.fileRead, fieldnames=self.fieldnames)
            return self.csvReader
        else:
            raise ValueError

    # Opens a CVS file and returns a csv.writer object:
    # example params: (<OUTPUT_CSV_FILE>, 'w')
    def openCSVFileWriter(self, filename, rw_attribute): 
        if isinstance(filename, str) and isinstance(rw_attribute, str):
            try:
                self.files.insert(0, open(filename, rw_attribute, newline='') )
                self.fileWrite = self.files[0]
            except IOError:
                raise IOError
            self.csvWriter = csv.DictWriter(self.fileWrite, fieldnames=self.fieldnames)
            self.csvWriter.writeheader()
            return self.csvWriter
        else:
            raise ValueError

    def setFieldNames(self, fieldnames):
        self.fieldnames = fieldnames

    # Returns the Postcode retrieved from a given row passed as parameter:
    def ReadRow(self, row_to_search):
        self.fileRead.seek(0)
        number_types = (int, complex)
        if isinstance(row_to_search, number_types):
            index = 1
            try: 
                for row in self.csvReader:
                    retrievedPostcode = row['postcode']
                    rowID = row['row_id']
                    if index == row_to_search:
                        return retrievedPostcode
                    index +=1
            except csv.Error as e:
                sys.exit('file {}, line{}: {}'.format(filename, self.csvReader.line_num, e))
        else:
            raise ValueError

    def WriteRow(self, row_id, postcode):
        pass

