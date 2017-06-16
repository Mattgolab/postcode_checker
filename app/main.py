# -*- coding: utf-8 -*-
# 12/05/17 Job application task
# 
# Author: Matthew Golab
# 
# Part 1 - Postcode validation, Please see Unit tests in ./test/test_postcodes.py
# Part 2 - Import CSV file containing postcode data, check each postcode for
#           validity and output bad postcodes to CSV file named "failed_validation.csv"

import app
import time

from app.postcode import Postcode

# Input / Output CSV filenames:
INPUT_CSV_FILE = "data/import_data.csv"
OUTPUT_CSV_FILE = "output/failed_validation.csv"

# Import CSV postcode file, test the postcode for validity.
# If it fails, output the postcode to a .csv file.
def ImportAndTest (postcodeObj):
    postcodeObj.setFieldNames(['row_id','postcode'])
    # Open a CSV file reader object:
    csvReaderObj = postcodeObj.openCSVFileReader(INPUT_CSV_FILE, 'rt', 'utf-8')
    # Open a CSV file writer:
    csvWriterObj = postcodeObj.openCSVFileWriter(OUTPUT_CSV_FILE, 'w')

    # Read the CSV file, line by line into a dict: 
    index = 0
    for row in csvReaderObj:
        retrievedPostcode = row['postcode']
        rowID = row['row_id']
        #Don't check the first row as this contains the csv header:
        if index is not 0:
            # Validate the postcode, if it fails write it to a csv file:
            result = postcodeObj.testPostCode(retrievedPostcode)
            if result == False:
                csvWriterObj.writerow({'row_id': rowID, 'postcode': retrievedPostcode})
        index +=1



print("Performing Import of CSV data and testing postcodes...")
postcode = Postcode()

# Initialise Postcode class with the regex to be used:
postcode.loadRegex(app.postcode.regular_expression)

# Start bulk import and test:
start_time = time.time()
ImportAndTest(postcode)
end_time = time.time()
print("Bulk import complete, Elapsed time (seconds): %s"% (end_time-start_time))
