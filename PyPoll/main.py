#import moduels
import os
import csv
#set path for file
dirname = os.path.dirname(__file__)
electioncsvpath = os.path.join("Resources", "Election_data.csv")
#declare variables
candidates = {}
total_votes = 0

with open(electioncsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)   
   for row in csvreader:
       total_votes = total_votes + 1
       if row[2] not in candidates:
           candidates[row[2]] = 1
       else:
           candidates[row[2]] = candidates [row[2]] + 1
print("Election Results")  
print("-----------------------------")        
print(f"Total Votes: {total_votes}")
print("-----------------------------")
max_votes = 0
winner = ""
for name,votes in candidates.items():
    print(f"{name}: {100*votes/total_votes:.1f}%: {votes}:")
    if votes> max_votes:
        winner = name
        max_votes = votes 
print(f"Winner: {winner}")