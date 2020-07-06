#import os and csv modules
import os
import csv

csvpath=os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#containers needed
candidate_list = []
total_votes = 0
candidate_votes = []
percent_of_votes = 0
# i=0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)


    for row in csvreader:
        candidate=row[2]
        candidate_votes.append(candidate)
        candidate_list.append(candidate)

        # if candidate not in candidate_list:
        #     candidate_list.append(candidate)
            # candidate_votes[candidate]=0
            # candidate_votes[candidate] +=1

allvotes = len(candidate_votes)
        
print("Election Results")
print("-------------------------")
print(f'Total Votes: {allvotes}')
print("-------------------------")

#List of candidates that received votes with percentage and number of votes

print(f'Winner: {candidate}')
print(f'Candidates: []')

    # print(f'CSV Header; {csv_header}')
    # for row in csvreader:
    #     total_votes = 0

    #     # # print(row)
    #     i=i+1
    #     if i>10:
    #         break

