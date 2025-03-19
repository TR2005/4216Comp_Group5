import csv
import pgeocode
print('This is test.py')
Country = pgeocode.Nominatim('us')
with open('USA Housing Dataset.csv', 'r') as f:
    Longitude=[]
    Latitude=[]
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    next(csv_reader)
    for row in csv_reader:
        data = row[16]
        zip = data[3:]
        Coordinates = Country.query_postal_code(zip)
        Longitude.append(Coordinates['longitude'])
        Latitude.append(Coordinates['latitude'])
    print(Latitude)
    print(Longitude)