# Lab 13: CSV-based payroll management system
import csv

filename = "employees.csv"

# Create a sample CSV file for demonstration
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "basic"])
    writer.writerow([101, "Asha", 30000])
    writer.writerow([102, "Ravi", 45000])
    writer.writerow([103, "Meena", 25000])

total_payout = 0

print("ID\tName\tGross\tDeduction\tNet")

with open(filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            basic = float(row["basic"])
        except ValueError:
            print("Invalid salary for", row["name"])
            continue

        hra = 0.20 * basic          # 20% house rent allowance
        da = 0.10 * basic           # 10% dearness allowance
        gross = basic + hra + da

        pf = 0.12 * basic           # 12% provident fund
        tax = 0.10 * gross if gross > 40000 else 0
        deductions = pf + tax

        net = gross - deductions
        total_payout += net

        print(row["id"], "\t", row["name"], "\t", gross, "\t", deductions, "\t", net)

print("\nTotal salary payout:", total_payout)
