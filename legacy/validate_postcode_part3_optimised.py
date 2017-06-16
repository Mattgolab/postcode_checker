# coding: utf-8
# 12/05/17 NHS Task
# 
# Author: Matthew Golab
#
# Part 3 - Postcode validation - Performance improvement


# Imports
import re
import csv
import time


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


# Note 1: I realise that optimisation is a requirement of Part 3, however whilst learning the Python language I found that
# compiling in the regular expression is the best method for optimisation.
# Note 2: To make the regular expression more readable over several lines, I have used ("""()""", re.X). 

# Compile in given regex and pass in using raw string notation (instead of string literal) with 'r'.
reValPostCode = re.compile(r"""(GIR\s0AA) | 
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
                                            # AA9A prefix
                                            ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]) |
                                            # A9A prefix
                                            ([A-PR-UWYZ][0-9][A-HJKPSTUW])
                                        )
                                    )
                                )
                                # 9AA suffix
                                \s[0-9][ABD-HJLNP-UW-Z]{2}
                            )""", re.X)

# Input / Output CSV filenames:
inputCsvFile = "./data/import_data.csv"
outputFailedCsvFile = "./output/failed_validation_unsorted.csv"
outputSucceededCsvFile = "./output/succeeded_validation_unsorted.csv"

outputFailedCsvFileSorted = "./output/failed_validation.csv"
outputSucceededCsvFileSorted = "./output/succeeded_validation.csv"

def TestPostCode(postcode):
    if not re.fullmatch(reValPostCode, postcode):
        return False
    else:
        return True

def performUnitTests ():
    failCount=0

    for postcode in UnitTestPostcodeData:
        unittestResult = TestPostCode(postcode[0])
        expectedResult = postcode[1]

        if unittestResult != expectedResult:
            resultString = "Fail"
            failCount += 1
        else:
            resultString = "Pass"

        if resultString == "Fail":
            print("Unit test \"%s\": Result: %s" % (postcode[2], resultString) )

    return failCount


def bulkImportAndTest ():
    fieldnames=['row_id','postcode']

    with open(outputFailedCsvFile, 'w') as csvOutFile:
        failedFileWriter = csv.DictWriter(csvOutFile, fieldnames)
        failedFileWriter.writeheader()

        with open(outputSucceededCsvFile, 'w') as csvOutFile:
            successFileWriter = csv.DictWriter(csvOutFile, fieldnames)
            successFileWriter.writeheader()

            with open(inputCsvFile, 'rt', encoding='utf-8') as csvFile:
                fileReader = csv.DictReader(csvFile, fieldnames=fieldnames)
                index = 0
                for row in fileReader:
                    retrievedPostcode = row['postcode']
                    rowID = row['row_id']
                    #Don't check the first row 
                    if index is not 0:
                        result = TestPostCode(retrievedPostcode)
                        if result == False:
                            failedFileWriter.writerow({'row_id': rowID, 'postcode': retrievedPostcode})
                        else:
                            successFileWriter.writerow({'row_id': rowID, 'postcode': retrievedPostcode})
                    index +=1


def sortCSVFile (csvFile, outputCSVFile):
    reader = csv.DictReader(open(csvFile, 'r'))
    result = sorted(reader, key=lambda d: float(d['row_id']))

    writer = csv.DictWriter(open(outputCSVFile, 'w'), reader.fieldnames)
    writer.writeheader()
    writer.writerows(result)



#######################################################################
#   Start of script:

print("Testing regular expression using unit tests...")
failureCount = performUnitTests()
print("Test complete, unit test failure count: %d."% failureCount)

# If unit tests have passed continue with bulk import:
if not failureCount:
    print("")
    print("Part 3: Performing Bulk import and test...")
    start_time = time.time()
    bulkImportAndTest()

    print("Sorting files...")
    sortCSVFile(outputFailedCsvFile, outputFailedCsvFileSorted)
    sortCSVFile(outputSucceededCsvFile, outputSucceededCsvFileSorted)

    end_time = time.time()
    print("Elapsed time (seconds): %s"% (end_time-start_time) )

    print("Finished test, results are in CSV files:")
    print("%s" % (outputFailedCsvFileSorted))
    print("%s" % (outputSucceededCsvFileSorted))

    print("Unsorted (raw data) CSV files:")
    print("%s" % (outputFailedCsvFile))
    print("%s" % (outputSucceededCsvFile))

