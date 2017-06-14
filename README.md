# postcode_checker
This task was required as part of a job application and revolves around creating unit tests to validate a regular expression that in itself validates postcodes.

Postcode data is of the following format:  
|row_id	| postcode |  
|-------|----------|  
|1		| BD3 4NN  |  
|2		| BD20 2BR |  

The actual download of postcodes (import_data.csv) had approx. 2 million postcodes, to reduce filesizes I have uploaded a sample of 300,000:

# Task Instructions - Readme

## Pre-requisites
My Python code was run in the following environment(s):
* Linux Ubuntu 14.04.1, using Python 3.4.
* Windows 10, using Python 3.6.

## Running the python script: 

set PYTHONPATH=%PYTHONPATH%;<PATH_TO_GIT_PROJECT>/

### Executing Part 1  
To run unit tests for the postcode test data perform the following:

cd <ROOT_PATH_OF_SCRIPTS>  
python3 ./validate_postcode_part1.py
  
#### General Notes  
  1. In part 1, I had already optimised the way the regular expression is loaded into the "re" module, by compiling it in upon decalring it. 
     I realise that optimisation is a requirement of Part 3, however whilst learning the Python language I found that compiling in the regular expression is the best method for optimisation.  
  2. To make the regular expression more readable over several lines, I have used ("""()""", re.X). 

#### Improvements that can be made:

  1. I could use the in-built "unittest" module to create unit tests that use the postcode test data. This would have the benefit of using developing using TDD processes and also leveraging the Object Oriented abilities of the Python langauge. 
  However I have no prior experience of Python and I thought I would keep things simple and leave that for future development.
    
  2. The postcode test data could be placed into a CSV file, streamlining the code.  

### Executing Part 2
To perform bulk import:
Note: Ensure "import_data.csv" file has been untar'ed into the root path of the script  

cd <ROOT_PATH_OF_SCRIPTS>  
python3 ./validate_postcode_part2.py   

The "failed_validation.csv" is output to the root of the script.  
  
### Executing Part 3
Perform the following commands:  

cd <ROOT_PATH_OF_SCRIPTS>  
python3 ./validate_postcode_part3_initial_imp.py  

... to run the optimised version:    
python3 ./validate_postcode_part3_optimised.py 

#### Part 3 - Analysis of optimisation

To measure improvements in the optimisation I used the "time" module to count the amount of time that had elapsed from start to finish.

I tried to optimised the regular expression by changing the order in which conditionals are executed.  
Taking advantage of postcode districts that may have fewer postcodes due to their geographical size, such as Gibraltar, I was able to reduce the time taken from 121 seconds down to 94 seconds, so approximately 25% reduction in time.


