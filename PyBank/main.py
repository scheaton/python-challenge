import os   # Allow us to create file paths across op systems
import csv  # Module for reading CSV files

months = 0
total_pl = 0
max_increase = 0
max_decrease = 0

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)         #go past header
    for row in csvreader:
        months += 1
        pl = int(row[1])    # pl = Profit/Losses
        total_pl += pl
        if pl > max_increase :
            max_increase = pl
            max_increase_date = row[0]
        if pl < max_decrease :
            max_decrease = pl
            max_decrease_date = row[0]

report = ("Financial Analysis\n--------------------------------\n\
Total Months: %d\nTotal: %d\nAverage Change: $%.2f\n\
Greatest Increase in Profits: %s ($%d)\n\
Greatest Decrease in Profits: %s ($%d)"\
% (months, total_pl, total_pl/months, max_increase_date, \
max_increase, max_decrease_date, max_decrease))

print(report)

output_path = os.path.join(".", "Analysis", "Analysis.txt")

with open(output_path, 'w') as f:
    f.write(report)