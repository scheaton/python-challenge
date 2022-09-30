import os   # Allow us to create file paths across op systems
import csv  # Module for reading CSV files

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)# save and go past header

    row = next(csvreader)   # Treat month differently
    months = 1              # because some of our stats
    total_pl = int(row[1])  # are about changes.
    total_pl_change = 0
    max_increase = 0
    max_decrease = 0
    prev_pl = int(row[1])
    
    for row in csvreader:
        months += 1
        total_pl += int(row[1])
        pl_change = int(row[1]) - prev_pl   # pl = Profit/Losses
        total_pl_change += pl_change
        if pl_change > max_increase :
            max_increase = pl_change
            max_increase_date = row[0]
        if pl_change < max_decrease :
            max_decrease = pl_change
            max_decrease_date = row[0]
        prev_pl = int(row[1])

report = ("'''text\nFinancial Analysis\n-----------------------------\n\
Total Months: %d\nTotal: $%d\nAverage Change: $%.2f\n\
Greatest Increase in Profits: %s ($%d)\n\
Greatest Decrease in Profits: %s ($%d)\n'''"\
% (months, total_pl, total_pl_change/(months-1), max_increase_date, \
max_increase, max_decrease_date, max_decrease))

print(report)

output_path = os.path.join(".", "analysis", "Analysis.txt")

with open(output_path, 'w') as f:
    f.write(report)

# print(header)