#import dependencies
import csv
import datetime

#load data for analysis
data = 'employee_data1.csv'

#dictionary of us states with abbreviations to convert states in our file to their abbreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#create empty lists to hold the new data after it is formatted
empIDs = []
first_name = []
last_name = []
state = []
dob = []
ssn = []

with open(data,'r') as csvdata:
    employee_data = csv.DictReader(csvdata,delimiter=',')
#loop through data and reformat as required
    for row in employee_data:
        #split the full name into first and last name and add to empty list above
        split_name = row["Name"].split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])
        
        empIDs.append(row["Emp ID"])

        #convert full state name to abbreviation
        state.append(us_state_abbrev[row["State"]])
        
        #split ssn and reformat to show only last 4
        split_ssn = row["SSN"].split("-")
        split_ssn[0] = "* * *"
        split_ssn[1] = "* *"
        new_ssn = "-".join(split_ssn)
        ssn.append(new_ssn)
        
        #reformat dob and add to empty list
        dob_formatted = datetime.datetime.strptime(row["DOB"],"%Y-%m-%d").strftime("%d/%m/%Y")
        dob.append(dob_formatted)

#zip the lists above to create our new reformated data
new_file = zip(empIDs,first_name,last_name,dob,ssn,state)

#write the new data to a new file
with open('new_data_file','w') as new_data:
    writer = csv.writer(new_data)
    writer.writerow(['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    writer.writerows(new_file)        