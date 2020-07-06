#import the os and csv modules
import os
import csv

#Containers needed
month_count=[]
profit_total = []
profit_sum = 0
profit_change = []
average_changes = 0
                                                
#Reading csv file:

csvpath = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyBank\\Resources\\PyBank_Resources_budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Total number of months included in dataset

    for row in csvreader:
        date =row[0]
        profit=row[1]
        month_count.append(date)
        profit_total.append(profit)
        profit_change.append(profit)

totalmonth = len(month_count)

print ("Company Profit Loss")
print ("--------------------")

print(f' Total Months: {totalmonth}')

# WORKS TILL THIS POINT, DO NOT CHANGE

for i in range(0, len(profit_total)):
    profit_sum=profit_sum + int(profit_total[i])

print (f'Total Earnings: ${profit_sum}')


# Average of the changes in "profit/loss" over the entire period
# Greatest increase in profits (date and amount) over the entire period
# greatest decrease in losses (date and amount) over the entire period

