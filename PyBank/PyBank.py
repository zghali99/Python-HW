
import os
import csv
import statistics

total_months = 0
total = 0
pre_rev = 0
rev_change = 0
rev_changes = []
avg_change = 0
greatest_increase = 0
greatest_decrease = 0

budget_data = os.path.join('..','PyBank','Resources', 'budget_data.csv')

with open(budget_data) as CSV_file:
    readCSV = csv.reader(CSV_file, delimiter=',')
    first = next(readCSV)

    for row in readCSV:
        total_months = total_months + 1
        total = total + int(row[1])
        rev_change = int(row[1]) - pre_rev
        pre_rev = int(row[1])
        rev_changes = rev_changes + [rev_change]
        avg_change = statistics.mean(rev_changes)

       # if rev_change > greatest_increase[1]:
       #     greatest_increase[1] = rev_change
       #     greatest_increase[0] = row[1]

       # elif rev_change < greatest_decrease[1]:
       #     greatest_decrease[1] = rev_change
       #     greatest_decrease[0] = row[1]


print("Financial Analysis")
print("---------------------------------")
print('Total Months: $ ', total_months)
print("Total: ", total)
print("Average Change: ", avg_change)
#print("Greatest Increase in Profits: ", Date[i], "(", greatest_increase + ")")
#print("Greatest Decrease in Profits: ", Date[i], "(", greatest_decrease + ")")