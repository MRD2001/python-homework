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

# Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")

# Set the path using Pathlib
csvpath = Path('../PyBank/budget_data.csv')

# Initialize variables
customer_total = 0
day_count = 0
line_num = 0

with open(csvpath, 'r') as csvfile:
    
    # Print the datatype of the file object
    print(type(csvfile))
    
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader)
    
     
    