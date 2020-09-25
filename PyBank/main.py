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

with open(budgetcsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)   
   for row in csvreader:
       total_months += 1
   print(total_months) 

with open(budgetcsvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)
   for row in csvreader:
        net_total += float(row[1])
    
   print(net_total)

with open(budgetcsvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    for row in csvreader:
        profit_loss.append(int(row[1]))
        months.append(row[0])

    for i in range(1,len(profit_loss)):
        change.append((int(profit_loss[i]) - int(profit_loss[i-1])))

    average_change = sum(change)/ len(change)

    print(average_change)

# def financial_analysis(budget_data):
#     month = str(budget_data[0])
#     profit_loss = int(budget_data[1])
#     total_months = len(month)
#     net_total = []
#     net_total.append(int(profit_loss) + int(profit_loss + 1))
#     change = []
#     change.append(int(profit_loss) - int(profit_loss - 1))
#     average_change = (sum(change)/ len(change)
#     greatest_increase = max(average_change)
#     greatest_decrease = min(average_change)
#     print(f"Financial Analysis")
#     print(f"______________________________________________________________________________________")
#     print(f"Total months:   {str(total_months)}")
#     print(f"Total:   ${str(net_total)}")
#     print(f"Average change:   ${str(average_change)}")
#     print(f"Greatest Increase in Profits:   {str(month[average_change.index(Greatest_increase))+1])}  ${str(greatest_increase)}")
#     print(f"Greatest Decrease in Profits:  {str(month[average_change.index(Greatest_decrease))+1])}  ${str(greatest_decrease)}"))
#     # output to a text file
#    # file = open("output.txt","w")
#    # file.write("Financial Analysis" + "\n")
#    # file.write("...................................................................................." + "\n")
#    # file.write("total months: " + str(total_months) + "\n")
#    # file.write("Total: " + "$" + str(sum(P)) + "\n")
#    # file.write("Average change: " + "$" + str(revenue_average) + "\n")
#    # file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
#    # file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
#    # file.close()
# with open(budgetcsvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     next(csvreader, None)
#     for row in csvreader:
#         financial_analysis(row)