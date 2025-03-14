import csv
print('This is test.py')
with open('USA Housing Dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    next(csv_reader)
    for row in csv_reader:
        print(row)