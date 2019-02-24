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
"""

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables
empID = []
nameFull = []
name = []
nameFirst = []
nameLast = []
DOB = []
date = []
SSN = []
SSN_string = []
state = []
i = 0

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
        empID.append(row[0])
        nameFull.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])

# Split first and last names into nameFirst and nameLast lists
while i < len(nameFull):
    name = nameFull[i].split(" ")
    nameFirst.append(name[0])
    nameLast.append(name[1])
    i += 1

# Reset iterator
i = 0

# Reformat date of birth
while i < len(DOB):
    date = DOB[i].split("-")
    DOB[i] = date[1] + '/' + date[2] + '/' + date[0]
    i += 1

# Reset iterator
i = 0

# Reformat SSN
while i < len(SSN):
    SSN_string = SSN[i].split("-")
    SSN[i] = "***-**-" + SSN_string[2]
    i += 1

# Reset iterator
i = 0

# Create State abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Reformat State name
while i < len(state):
    state[i] = us_state_abbrev[state[i]]
    i += 1

# Reset iterator
i = 0

 #--------------------------------------------------------

# Set output file
output_path = os.path.join("results.csv")

with open(output_path, 'w', newline='') as csvfile:
    
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    
    # Write data
    while i < len(empID):
        csvwriter.writerow([empID[i], nameFirst[i], nameLast[i], DOB[i], SSN[i], state[i]])
        i += 1