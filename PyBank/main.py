import os
import csv
import pandas as pd 

csvpath = os.path.join('budget_data_2.csv')
# Open the file to be analyze

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
# Create panda data frame to analyze data    
    csvfile_pd = pd.read_csv(csvpath)

# Calculate the total number of months in the file, assuming no duplicates
    total_number_months = csvfile_pd['Date'].count()

# Calculate total revenue
    total_revenue = csvfile_pd['Revenue'].sum()

# Calculate average revenue across the entire period
    average_revenue = csvfile_pd['Revenue'].mean()

# Calculate the difference in revenue between months
    monthly_rev_diff = csvfile_pd['Revenue'].diff()

# Calculate the average of the differences between months
    average_rev_change = monthly_rev_diff.mean()

# Add column to dataframe which holds the monthly differences
    csvfile_pd['Revenue Change'] = monthly_rev_diff

# Find the greatest increase in that column
    greatest_increase = csvfile_pd['Revenue Change'].max()

# Isolate the month that has the greatest increase
    greatest_month_row = csvfile_pd.loc[csvfile_pd['Revenue Change'] == greatest_increase]
# Create series to hold data for the mx month
    greatest_month = greatest_month_row.iloc[0]

# Find the greatest decrease in that column
    greatest_decrease = csvfile_pd['Revenue Change'].min()
# Isolate the month
    least_month_row = csvfile_pd.loc[csvfile_pd['Revenue Change'] == greatest_decrease]

    least_month = least_month_row.iloc[0]

# Export file to excel
csvfile_pd.to_excel('Resources/PyBank.xlsx', index=False)

# Display the information being requested after analysis

    print('Financial Analysis')
    print('----------------------------------------------------------')
    print('Total Months: ' + str(total_number_months))
    print('Total Revenue: $' + str(total_revenue))
    print('Average Revenue Change: $' + str(int(average_rev_change)))
    print('Greatest Increase in Revenue: ' + greatest_month[0] + ' $' + str(int(greatest_increase)))
    print('Greatest Decrease in Revenue: ' + least_month[0] + ' $' + str(int(greatest_decrease)))
    print('----------------------------------------------------------')
    