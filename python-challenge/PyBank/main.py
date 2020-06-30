#import the os module
import os

#import the csv module
import csv
csvpath = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyBank\\Resources\\PyBank_Resources_budget_data.csv")

#Reading csv file:
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # Read header row first
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
        print(row)

# Total number of months included in dataset
# Net total amount of "profit/loss" over entire period
# Average of the changes in "profit/loss" over the entire period
# Greatest increase in profits (date and amount) over the entire period
# greatest decrease in losses (date and amount) over the entire period

