"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                 '
'CWRU Data Analytics                                  Robert Wood '
'                                                                 '
'                                                                 '
'Unit 3 | Assignment (Extra Content) - PyBoss            3/2/2019 '
'                                                                 '
'                                                                 '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

PyBoss

In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0,
a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation.
The company recently decided to purchase a new HR system, 
and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format
Your script will need to do the following:

Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:


Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

Then convert and export the data to use the following format instead:


Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA


In summary, the required conversions are as follows:


The Name column should be split into separate First Name and Last Name columns.
The DOB data should be re-written into MM/DD/YYYY format.
The SSN data should be re-written such that the first five numbers are hidden from view.
The State data should be re-written as simple two-letter abbreviations.


Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.
"""

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Define path of our .csv file
csvpath = os.path.join('Resources', 'employee_data.csv')

# With the file open
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
