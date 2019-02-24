"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                 '
'CWRU Data Analytics                                  Robert Wood '
'                                                                 '
'                                                                 '
'Unit 3 | Assignment - PyPoll                            3/2/2019 '
'                                                                 '
'                                                                 '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables
totalVotes = 0
candidate = []
candidateVotes = []
nameSummary = []
voteSummary = []
Results = []
i = 0
j = 0
k = 0

# Define path of our .csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# With the file open
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        candidateVotes.append(row[0])
        candidate.append(row[2])
    
# While loop to summarize candidates and associated votes    
while i < totalVotes:
    # If candidate name already is in summary table, increment vote count
    if candidate[i] in nameSummary:
        counter = int(nameSummary.index(candidate[i]))
        voteSummary[counter] = int(voteSummary[counter]) + 1
    # If candidate name is NOT already in summary table, add the name and set associated vote count to 1
    else:
        nameSummary.append(candidate[i])
        voteSummary.append("1")
    i += 1

# Determine winner (use index of the maximum voteSummary value to find the associated name in nameSummary)
winner = nameSummary[voteSummary.index(max(voteSummary))]

#--------------------------------------------------------

# Print Results to terminal
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {totalVotes:,}")
print("-------------------------")

# Loop to print summaries
while j < len(nameSummary):
    print(f"{nameSummary[j]}: {'{:.3%}'.format(voteSummary[j] / totalVotes)} ({voteSummary[j]:,})")
    j += 1
    
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#--------------------------------------------------------

# Create results .txt file
file = open("results.txt", "w+")

# Write results to text file
file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {totalVotes:,}\n")
file.write("-------------------------\n")

# Loop to print summaries
while k < len(nameSummary):
    file.write(f"{nameSummary[k]}: {'{:.3%}'.format(voteSummary[k] / totalVotes)} ({voteSummary[k]:,})\n")
    k += 1
    
file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------")

# Close .txt file
file.close()