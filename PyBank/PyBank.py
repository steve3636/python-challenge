import csv

def PyBank_budget_data(csv_file):
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        total_months, net_total = 0, 0
        prev_profit_loss = None
        profit_loss_changes = []
        greatest_increase = {"date": "", "amount": 0}
        greatest_decrease = {"date": "", "amount": 0}

        for row in csv_reader:
            total_months += 1
            net_total += int(row['Profit/Losses'])

            current_profit_loss = int(row['Profit/Losses'])
            if prev_profit_loss is not None:
                change = current_profit_loss - prev_profit_loss
                profit_loss_changes.append(change)

                if change > greatest_increase["amount"]:
                    greatest_increase = {"date": row['Date'], "amount": change}

                if change < greatest_decrease["amount"]:
                    greatest_decrease = {"date": row['Date'], "amount": change}

            prev_profit_loss = current_profit_loss

    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
    return total_months, net_total, average_change, greatest_increase, greatest_decrease

csv_file_path = 'budget_data.csv'
total_months, net_total, average_change, greatest_increase, greatest_decrease =PyBank_budget_data(csv_file_path)

print("Total months:", total_months)
print("Net total of Profit/Losses:", net_total)
print("Average change:", average_change)
print("Greatest increase in profits:")
print("  Date:", greatest_increase["date"])
print("  Amount:", greatest_increase["amount"])
print("Greatest decrease in profits:")
print("  Date:", greatest_decrease["date"])
print("  Amount:", greatest_decrease["amount"])
