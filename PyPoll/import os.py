import os
import csv

# Create the CSV file path using os.path.join
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Print the CSV file path
print(csvpath)

# Open the CSV file in read mode and create a csv.reader object
with open(csvpath, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Print the csvreader object (will show a representation of the reader)
    print(csvreader)

    # Read the first row as the CSV header
    csv_header = next(csvreader)

    # Print the CSV header to display the column names
    print(f"CSV_Header: {csv_header}")

    # Iterate through the csvreader and print each row
    for row in csvreader:
        print(row)