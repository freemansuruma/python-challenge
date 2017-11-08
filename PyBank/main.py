import os
import csv
import pandas as pd 

csvpath = os.path.join('budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csvfile_pd = pd.read_csv(csvpath)

    total_number_months = csvfile_pd['Date'].count()

    total_revenue = csvfile_pd['Revenue'].sum()

    average_revenue = csvfile_pd['Revenue'].mean()
    