import csv
import os
import pandas as pd

file_path = os.path.join('election_data_2.csv')

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    file_path_pd = pd.read_csv(file_path)

# Find the total votes cast
    total_votes_cast = file_path_pd['Voter ID'].count()

# Find the number of candidates
    candidates = file_path_pd['Candidate'].unique()

# Find the number of votes for each candidate
    total_votes_per_candidate = file_path_pd['Candidate'].value_counts()
# Sort the list so that the candidate with the most votes is the first item    
    total_votes_per_candidate.sort_values(ascending=False)

# Find the percentage of votes for each candidate
    pct_votes_per_candidate = (total_votes_per_candidate/total_votes_cast)*100

#Convert the series to lists
    candidates_list = candidates.tolist()

    votes_list = total_votes_per_candidate.tolist()

    pct_list = pct_votes_per_candidate.tolist()

# Display the information required

    print('Election Results')
    print('-----------------------------------------')
    print('Total Votes: ' + str(total_votes_cast))
    print('-----------------------------------------')
    i = 0
    for item in candidates_list:
    
        print(item + ': ' + str(round(pct_list[i])) + '% ' + '(' + str(votes_list[i]) + ')')
        i=+1

    print('-----------------------------------------')
    print('Winner: ' + str(candidates_list[0]))