import csv
import pgeocode
import numpy as np
import matplotlib.pyplot as plt
print('This is test.py')
Country = pgeocode.Nominatim('us')
with open('USA Housing Dataset.csv', 'r') as f:
    Longitude = []
    Latitude = []
    Colour=[]
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    next(csv_reader)
    for row in csv_reader:
        FullZip = row[16]
        Price = float(row[1])
        Zip = FullZip[3:]
        Coordinates = Country.query_postal_code(Zip)
        Longitude.append(Coordinates['longitude'])
        Latitude.append(Coordinates['latitude'])
        #Sorting all Houses into 200 Thousand price brackets
        if Price >= 200000:
            Colour.append('green ')
        elif Price >= 400000:
            Colour.append('red ')
        elif Price >= 600000:
            Colour.append('blue ')
        elif Price >= 800000:
            Colour.append('purple ')
        elif Price >= 1000000:
            Colour.append('pink ')
        elif Price >= 1200000:
            Colour.append('orange ')
        elif Price >= 1400000:
            Colour.append('brown ')
        elif Price >= 1600000:
            Colour.append('gray ')
        elif Price >= 1800000:
            Colour.append('olive ')
        elif Price >= 2000000:
            Colour.append('cyan ')
        else:
            Colour.append('k ')
x = Longitude
y = Latitude
plt.scatter(x,y)
plt.show()