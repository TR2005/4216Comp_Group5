import csv
with open('Mobiles Dataset (2025).csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    
