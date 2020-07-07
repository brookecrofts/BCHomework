#import os and csv modules
import os
import csv

csvpath=os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#containers needed
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
total_votes = 0
candidate_votes = {}
percent_of_votes = 0
total_votes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)


    for row in csvreader:
        candidate=row[2]
        total_votes.append(candidate)
        candidate_list.append(candidate)

        if (candidate in candidate_votes):
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1
       

    list(candidate_votes.keys())
    candidate_list = list(candidate_votes.keys())
    Kahnvotes = candidate_votes['Khan']
    Correyvotes = candidate_votes['Correy']
    Livotes = candidate_votes['Li']
    Otooleyvotes = candidate_votes["O'Tooley"]

allvotes = len(total_votes)

print("Election Results")
print("-------------------------")
print(f'Total Votes: {allvotes}')
print("-------------------------")

#List of candidates that received votes with percentage and number of votes

print(f'Khan: {Kahnvotes}')
print(f'Correy: {Correyvotes}')
print(f'Li: {Livotes}')
print(f'OTooley: {Otooleyvotes}')
print("--------------------------")
# print(f'Winner: {candidate}')


# output_path = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Analysis\\outputone.txt")
# with open(output_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=' ')

#     csvwriter.writerow("Election Results")
#     csvwriter.writerow("--------------------")



    #     # # print(row)
    #     i=i+1
    #     if i>10:
    #         break

