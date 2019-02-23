"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                 '
'CWRU Data Analytics                                  Robert Wood '
'                                                                 '
'                                                                 '
'Unit 3 | Assignment - PyBank                            3/2/2019 '
'                                                                 '
'                                                                 '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Initialize variables
monthCount = 0
Total = 0
averageChange = 0
greatestIncrease = 0
greatestDecrease = 0
dateList = []
moneyList = []
change = []
i = 0

# Define path of our .csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# With the file open
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        monthCount += 1
        Total += int(row[1])
        dateList.append(row[0])
        moneyList.append(row[1])
    
    # While loop to populate a new list "change" with the difference between subsequent months    
    while i < len(moneyList)-1:
        difference = int(moneyList[i+1]) - int(moneyList[i])
        change.append(difference)
        i += 1
    
    # Set Greatest Increase amount and month/year    
    greatestIncrease = int(max(change))
    greatestIncreaseMo = dateList[int(change.index(max(change)))+1]
    
    # Set Greatest Decrease amount and month/year
    greatestDecrease = int(min(change))
    greatestDecreaseMo = dateList[int(change.index(min(change)))+1]
    
    # Set Average Change
    averageChange = round(sum(change) / float(len(change)),2)
    
# Print Results
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${Total:,}")
print(f"Average Change: ${averageChange:,}")
print(f"Greatest Increase in Profits: {greatestIncreaseMo} (${greatestIncrease:,})")
print(f"Greatest Decrease in Profits: {greatestDecreaseMo} (${greatestDecrease:,})")

# Create results .txt file
file = open("results.txt", "w+")

# Write results to text file
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {monthCount}\n")
file.write(f"Total: ${Total:,}\n")
file.write(f"Average Change: ${averageChange:,}\n")
file.write(f"Greatest Increase in Profits: {greatestIncreaseMo} (${greatestIncrease:,})\n")
file.write(f"Greatest Decrease in Profits: {greatestDecreaseMo} (${greatestDecrease:,})")

# Close .txt file
file.close()
