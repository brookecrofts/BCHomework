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
    winner = max(candidate_list)

allvotes = len(total_votes)
Kahn_percent = (candidate_votes['Khan']/allvotes)*100
Correy_percent = (candidate_votes['Correy']/allvotes)*100
Li_percent = (candidate_votes['Li']/allvotes)*100
Otooley_percent = (candidate_votes["O'Tooley"]/allvotes)*100

print("Election Results")
print("-------------------------")
print(f'Total Votes: {allvotes}')
print("-------------------------")

#List of candidates that received votes with percentage and number of votes

print(f'Khan: ({Kahn_percent}{0:.0%}),{Kahnvotes}')
print(f'Correy: ({Correy_percent}%),{Correyvotes}')
print(f'Li: ({Li_percent}%),{Livotes}')
print(f'OTooley: ({Otooley_percent}%),{Otooleyvotes}')
print("--------------------------")
print(f'Winner: {winner}')


output_path = os.path.join("C:\\Users\\brook\\OneDrive\\Documents\\BootCamp\\Python\\BCHomework\\python-challenge\\PyPoll\\Analysis\\outputone.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow("Election Results")
    csvwriter.writerow("--------------------")
    csvwriter.writerow(f'Total Votes: {allvotes}')
    csvwriter.writerow("--------------------")
    csvwriter.writerow(f'Khan: ({Kahn_percent}{0:.0%}),{Kahnvotes}')
    csvwriter.writerow(f'Correy: ({Correy_percent}%),{Correyvotes}')
    csvwriter.writerow(f'Li: ({Li_percent}%),{Livotes}')
    csvwriter.writerow(f'OTooley: ({Otooley_percent}%),{Otooleyvotes}')
    csvwriter.writerow("--------------------------")
    csvwriter.writerow(f'Winner: {winner}')

