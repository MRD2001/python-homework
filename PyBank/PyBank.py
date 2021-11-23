"""
This Python file is the solution to the homework of Week2

@@ The solution is already found in stackoverflow website

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

the final script should print the analysis to the terminal and export a text file with the results.
"""
from pathlib import Path
import csv

# get the CSV file including the data.
file_to_load = "budget_data.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total : $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

# write the results into the text file
file_to_write = "fin_analysis.txt"
with open(file_to_write) as fin:
    fout = open(file_to_write,'w')
    fout.write('Financial Analysis\n')
    fout.write('--------------------------\n')
    number_months = len(date)
    fout.write('Total Months  :' + str(number_months) + '\n')
    fout.write('Total         : $' + str(sum(revenue)) + '\n')
    fout.write('Average change: $' + str(round(avg_rev_change,2)) + '\n')
    fout.write('Greatest Increase In Profits : On ' + str(max_rev_change_date) + ' By $ ' + str(round(max_rev_change,2)) + '\n')
    fout.write('Greatest Decrease In Profits : On ' + str(min_rev_change_date) + ' By $ ' + str(round(min_rev_change,2)) + '\n')
    for line in fin:
        fout.write('Test: ' + line.strip() + ' -t\n')
    fout.close()

