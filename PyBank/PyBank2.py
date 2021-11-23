"""
Your task is to create a Python script that analyzes the records to calculate each of the following:

The input is a CSV File with two columns , month (date format) and Amount for P/L for that month.

 * The total number of months included in the dataset.
 * The net total amount of Profit/Losses over the entire period.
 * The average of the changes in Profit/Losses over the entire period.
 * The greatest increase in profits (date and amount) over the entire period.
 * The greatest decrease in losses (date and amount) over the entire period.
 
 The Result should look like this
 
 Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)


"""
# From the pathlib library, import the main class Path
from pathlib import Path
import csv

# Set the path using Pathlib
csvpath = Path('../pyBank/budget_data.csv')
total_PL = 0
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
    #skip header row before counting
    next(csvreader,None)
    
    # Calculate the number of months exist in the file, which is actually the number of rows
    total_months = len(list(csvreader))
print(total_months)
    # Calculate the total amount of Profit/Losses throught the total period
    # Why do I need to open the file again ?
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
    #skip header row before counting
    next(csvreader,None)
    for row in csv.reader(csvfile):
        total_PL += int(row[1])
        
    print(total_PL)

# Calculate the average change in the Profit/loasses amount
change =0
value=0

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')
    #skip header row before counting
    next(csvreader,None)
    for row in csvfile:
        value= int(row[1])
        print(value)
        





