#import the os and csv modules
import os
import csv

#Containers needed
month_count=[]
profit_total = []
profit_sum = 0
profit_change = []
average_changes = 0
average_sum = []
                                                
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

print(f'Total Months: {totalmonth}')

for i in range(0, len(profit_total)):
    profit_sum=profit_sum + int(profit_total[i])

print (f'Total Earnings: ${profit_sum}')

# Average of the changes in "profit/loss" over the entire period
for i in range(0, len(profit_total)-1):
    profit_change[i] = float(profit_total[i]) - float(profit_total[i+1])
    
average_changes = [float(profit_total[i+1]) - float(profit_total[i]) for i in range (len(profit_total)-1)]
average_sum = sum(average_changes) / (totalmonth -1)
print(f'Average Change: ${average_sum}')

# Greatest increase/decrease in profits (date and amount) over the entire period
index=0
max_value = max(average_changes)
maxIndex = (average_changes.index(max_value)+1)
maxMonth = month_count[maxIndex]
min_value = min(average_changes)
minIndex = (average_changes.index(min_value)+1)
minMonth = month_count[minIndex]

print(f'Greatest Increase in Profits: {maxMonth} ${max_value}')
print(f'Greatest Decrease in Profits: {minMonth} (${min_value})')

# write output file
output_path = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyBank\\Analysis\\output.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow("Company Profit Loss")
    csvwriter.writerow("--------------------")
    csvwriter.writerow(f'Total Months: {totalmonth}')
    csvwriter.writerow(f'Total Earnings: ${profit_sum}')
    csvwriter.writerow(f'Average Change: ${average_sum}')
    csvwriter.writerow(f'Greatest Increase in Profits: {maxMonth} ${max_value}')
    csvwriter.writerow(f'Greatest Decrease in Profits: {minMonth} (${min_value})')