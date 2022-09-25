import os   # This will allow us to create file paths across operating systems
import csv  # Module for reading CSV files

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    #print(f"Total number of months included in the dataset: {len(csvreader)}")