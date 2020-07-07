#import os and csv modules
import os
import csv

csvpath=os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#containers needed
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
# print(candidate_list)
total_votes = 0
candidate_votes = {}
percent_of_votes = 0
total_votes = []
# i=0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)


    for row in csvreader:
        candidate=row[2]
        total_votes.append(candidate)
        candidate_list.append(candidate)
        # candidate_list.count("Khan")

allvotes = len(total_votes)
# Khanvotes = candidate_list.count("Khan")

print("Election Results")
print("-------------------------")
print(f'Total Votes: {allvotes}')
print("-------------------------")

#List of candidates that received votes with percentage and number of votes


# print(f'Khan: {Kahnovotes}')
print(f'Correy: [candidate_list]')
print(f'Li: [candidate_list]')
print(f'OTooley: [candidate]')
print("--------------------------")
print(f'Winner: {candidate}')


# output_path = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Analysis\\outputone.txt")
# with open(output_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=' ')

#     csvwriter.writerow("Election Results")
#     csvwriter.writerow("--------------------")



    #     # # print(row)
    #     i=i+1
    #     if i>10:
    #         break

