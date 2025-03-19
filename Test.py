import csv
import pgeocode
print('This is test.py')
Country = pgeocode.Nominatim('us')
with open('USA Housing Dataset.csv', 'r') as f:
    Longitude2 = [], Longitude4 = [], Longitude6 = [], Longitude8 = [], Longitude10 = [], Longitude12 = [], Longitude14 = [], Longitude16 = [], Longitude18 = [], Longitude20 = [], Longitude20Plus = []
    Latitude2 = [], Latitude4 = [], Latitude6 = [], Latitude8 = [], Latitude10 = [], Latitude12 = [], Latitude14 = [], Latitude16 = [], Latitude18 = [], Latitude20 = [], Latitude20Plus = []

    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    next(csv_reader)
    for row in csv_reader:
        FullZip = row[16]
        Price = row[2]
        Zip = FullZip[3:]
        Coordinates = Country.query_postal_code(Zip)
        #Sorting all Houses into 200 Thousand price brackets
        if Price >= 200000:
            Longitude2.append(Coordinates['longitude'])
            Latitude2.append(Coordinates['latitude'])
        elif Price >= 400000:
            Longitude4.append(Coordinates['longitude'])
            Latitude4.append(Coordinates['latitude'])
        elif Price >= 600000:
            Longitude6.append(Coordinates['longitude'])
            Latitude6.append(Coordinates['latitude'])
        elif Price >= 800000:
            Longitude8.append(Coordinates['longitude'])
            Latitude8.append(Coordinates['latitude'])
        elif Price >= 1000000:
            Longitude10.append(Coordinates['longitude'])
            Latitude10.append(Coordinates['latitude'])
        elif Price >= 1200000:
            Longitude12.append(Coordinates['longitude'])
            Latitude12.append(Coordinates['latitude'])
        elif Price >= 1400000:
            Longitude14.append(Coordinates['longitude'])
            Latitude14.append(Coordinates['latitude'])
        elif Price >= 1600000:
            Longitude16.append(Coordinates['longitude'])
            Latitude16.append(Coordinates['latitude'])
        elif Price >= 1800000:
            Longitude18.append(Coordinates['longitude'])
            Latitude18.append(Coordinates['latitude'])
        elif Price >= 2000000:
            Longitude20.append(Coordinates['longitude'])
            Latitude20.append(Coordinates['latitude'])
        else:
            Longitude20Plus.append(Coordinates['longitude'])
            Latitude20Plus.append(Coordinates['latitude'])
    