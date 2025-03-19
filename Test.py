import csv
import matplotlib.pyplot as plt

print('This is test.py')
with open('USA Housing Dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    
    #attatching row 1 to a list so it can be used by matplotlib

    

    YearBuilt = []
    Price = []
    for row in csv_reader:
        data = row[12]
        data1 = row[1]
        YearBuilt.append(data)
        Price.append(data1)

    YearBuilt.sort()
    Price.sort
    

    fig, ax = plt.subplots()

    ax.plot(YearBuilt, Price)

    plt.show()

    

   




