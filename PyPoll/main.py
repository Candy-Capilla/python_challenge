#import modules
import os
import csv
#set path file
dirname = os.path.dirname(__file__)
electioncsvpath = os.path.join("Resources", "Election_data.csv")
#declare variables
candidates = {}
total_votes = 0
#open csv and skip header
with open(electioncsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)
#sum total votes and find candidates that received votes
   for row in csvreader:
       total_votes = total_votes + 1
       if row[2] not in candidates:
           candidates[row[2]] = 1
       else:
           candidates[row[2]] = candidates [row[2]] + 1
#create function to total candidate votes, declare winner, print results, and write to file
def candidate_votes(Election_data):
    output_file = os.path.join("Analysis", "Election_Results.txt")
    max_votes = 0
    winner = ""
    with open(output_file,"w") as file:
        file.write("Election Results")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Votes: {total_votes}")
        file.write("\n")
        file.write("-----------------------------")
        file.write("\n")
        print("Election Results")  
        print("-----------------------------")        
        print(f"Total Votes: {total_votes}")
        print("-----------------------------")
        for name,votes in candidates.items():
            file.write(f"{name}: {100*votes/total_votes:.3f}% ({votes})")
            file.write("\n")
            print(f"{name}: {100*votes/total_votes:.3f}% ({votes})")
            if votes > max_votes:
                winner = name
                max_votes = votes
        file.write("-----------------------------")
        file.write("\n")
        file.write(f"Winner: {winner}")
        file.write("\n")
        file.write("-----------------------------")
        print("-----------------------------")
        print(f"Winner: {winner}")
        print("-----------------------------")
#run function
candidate_votes(row)