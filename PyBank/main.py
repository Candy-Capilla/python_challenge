#import moduels
import os
import csv
#set path for file
dirname = os.path.dirname(__file__)
budgetcsvpath = os.path.join("Resources", "budget_data.csv")
#declare variables
total_months = 0
net_total = 0
months = []
change = []
profit_loss = []

print(f"Financial Analysis")
print(f"--------------------------")

with open(budgetcsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)   
   for row in csvreader:
       total_months += 1
       net_total += int(row[1])
       profit_loss.append(int(row[1]))
       months.append(row[0])

   print(f"Total Months: {total_months}") 

   print(f"Total: $ {net_total}")

   for i in range(1,len(profit_loss)):
        change.append((int(profit_loss[i]) - int(profit_loss[i-1])))

   average_change = sum(change)/ len(change)

   print(f"Average Change: {round(average_change,2)}")


greatest_increase = max(change)
greatest_decrease = min(change)


print(f"Greatest Increase: {months[change.index(max(change)) + 1]} (${(str(greatest_increase))})")
print(f"Greatest Decrease: {months[change.index(min(change)) + 1]} (${(str(greatest_decrease))})")

# location of open output files
output_file = os.path.join("Analysis", "Financial_Analysis_Summary.txt")
with open(output_file,"w") as file:

# Write output file
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${net_total}")
    file.write("\n")
    file.write(f"Average Change: {round(average_change,2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[change.index(max(change)) + 1]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[change.index(min(change)) + 1]} (${(str(greatest_decrease))})")
