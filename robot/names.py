import random
import csv

# Load lists of first names and last names (you can replace these with your own lists)
with open('/Users/pavankumar/VSCODE/test_cases_robot/robot/first_names.txt') as f:
    first_names = f.read().splitlines()

with open('/Users/pavankumar/VSCODE/test_cases_robot/robot/last_names.txt') as f:
    last_names = f.read().splitlines()

# Generate and write the names to a CSV file
num_names = 2000

with open('us_names.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['First Name', 'Last Name'])

    for _ in range(num_names):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        csv_writer.writerow([first_name, last_name])

print(f'{num_names} names written to "us_names.csv"')