# postcode_checker
This task revolves around creating unit tests to validate a regular expression that in itself validates postcodes.

Postcode data is of the following format:  
|row_id	| postcode |  
|-------|----------|  
|1      | BD3 4NN  |
|2      | BD20 2BR |

The download of postcodes resides in data/import_data.csv and consists of 2 million postcodes.  

# Task Instructions - Readme  

## Pre-requisites
My Python code was run in the following environment(s):
* Linux Ubuntu 14.04.1, using Python 3.4.
* Windows 10, using Python 3.6.

## Running the python scripts: 

### Set the environment variable

In Windows:  
set PYTHONPATH=%PYTHONPATH%;<PATH_TO_GIT_PROJECT>  

In Linux:  
export PYTHONPATH=$PYTHONPATH:<PATH_TO_GIT_PROJECT>

### Executing Part 1  
To run unit tests for the postcode test data perform the following:

cd <PATH_TO_GIT_PROJECT>  
<Set env variable as above>
py ./test/test_postcodes.py
  
#### General Notes  
  1. In part 1, I had already optimised the way the regular expression is loaded into the "re" module, by compiling it in upon declaring it. 
     I realise that optimisation is a requirement of Part 3, however whilst learning the Python language I found that compiling in the regular expression is the best method for optimisation.  
  2. To make the regular expression more readable over several lines, I have used ("""()""", re.X). 

#### Improvements made:

  1. I have used Pythons "unittest" module to create unit tests that use the postcode test data to test the regular expression.  
  2. The postcode test data could be placed into a CSV file, streamlining the code.  

### Executing Part 2  
To perform bulk import:  
Note: Ensure "import_data.csv" file has been untar'ed and placed into ./data/  

cd <PATH_TO_GIT_PROJECT>  
py ./app/main.py   

The "failed_validation.csv" file containing invalid postcodes is in the folder ./output/.  
  
### Executing Part 3
Perform the following commands:  
  
cd <ROOT_PATH_OF_SCRIPTS>  
python3 ./legacy/validate_postcode_part3_initial_imp.py  
  
... to run the optimised version:  
python3 ./legacy/validate_postcode_part3_optimised.py  
  
#### Part 3 - Analysis of optimisation  
  
To measure improvements in the optimisation of the regular expression, I used the "time" module to count the amount of time that had elapsed from start to finish.

I tried to optimised the regular expression by changing the order in which conditionals are executed.  
Taking advantage of postcode districts that may have fewer postcodes due to their geographical size, such as Gibraltar, I was able to reduce the time taken from 121 seconds down to 94 seconds, so approximately 25% reduction in time.


