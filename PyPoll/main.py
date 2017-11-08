import csv
import os
import pandas as pd

file_path = os.path.join('election_data_2.csv')

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    file_path_pd = pd.read_csv(file_path)

    total_votes_cast = file_path_pd['Voter ID'].count()

    candidates = file_path_pd['Candidate'].unique()

    total_votes_per_candidate = file_path_pd['Candidate'].value_counts()

    pct_votes_per_candidate = total_votes_per_candidate/total_votes_cast
    