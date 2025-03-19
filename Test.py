import csv
import pgeocode
import matplotlib.pyplot as plt
print('This is test.py')
Country = pgeocode.Nominatim('us')
Longitude = []
Latitude = []
Colour=[]
Ziplist=[]
Pricelist=[]
Appearancelist=[]
AvgPricelist=[]
with open('USA Housing Dataset.csv', 'r') as f:
    #initialising csv reader
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        FullZip = row[16]
        Price = float(row[1])
        #removing first 3 letters of the state zipcode
        Zip = FullZip[3:]
        if Zip in Ziplist:
            #getting location of zipcode in list and adding new price+appearance onto the same index in the releveant lists
            Location= Ziplist.index(Zip)
            Appearancelist[Location] = int(Appearancelist[Location])+1
            Pricelist[Location] = int(Pricelist[Location])+Price
        else:
            #adding the first instance for said zip and adding its price and an appearance to the lists
            Ziplist.append(Zip)
            Pricelist.append(int(Price))
            Appearancelist.append(int('1'))
            Coordinates = Country.query_postal_code(Zip)
            Longitude.append(Coordinates['longitude'])
            Latitude.append(Coordinates['latitude'])
print(Appearancelist)
i=0
#dividing all items in Price list with Apperance list to get the average house price
for item in Appearancelist:
    AvgPricelist.append(Pricelist[i]/Appearancelist[i])
    i=i+1
print(AvgPricelist)
#sorting average house price into 200k ranges and assigning it a colour on the graph 
i=0
for item in AvgPricelist:
    if AvgPricelist[i] <= 200000:
        Colour.append('green')
    elif AvgPricelist[i] <= 400000:
        Colour.append('red')
    elif AvgPricelist[i] <= 600000:
        Colour.append('blue')
    elif AvgPricelist[i] <= 800000:
        Colour.append('purple')
    elif AvgPricelist[i] <= 1000000:
        Colour.append('pink')
    elif AvgPricelist[i] <= 1200000:
        Colour.append('orange')
    elif AvgPricelist[i] <= 1400000:
        Colour.append('brown')
    elif AvgPricelist[i] <= 1600000:
        Colour.append('gray')
    elif AvgPricelist[i] <= 1800000:
        Colour.append('olive')
    elif AvgPricelist[i] <= 2000000:
        Colour.append('cyan')
    else:
        Colour.append('black')
    i=i+1
x = Longitude
y = Latitude
plt.scatter(x,y, c=Colour)
plt.show()