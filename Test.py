import csv
import pgeocode
import matplotlib.pyplot as plt
print('This is test.py')
#Defining menu function for callback on incorrect input
def Menu():
    print(f"Please input whos part of the project you wish to run\n1.Reece\n2.Tomos\n3.Oliver\n4.Sam")
    Selection = input()
    if Selection == 1:
        Reece()
    elif Selection == 2:
        Tomos()
    elif Selection == 3:
        Oliver()
    elif Selection == 4:
        Sam()
    else:
        print("incorrect input please try again")
        Menu()
#Executing menu code block
Menu()

#Defining a function to be execute Code made by Tomos for simplicity of Menu function
def Tomos():
    #defining variables and arrays
    Country = pgeocode.Nominatim('us')
    HousePrice = []
    HouseFloorNumber = []
    HouseFloorAppearance = []
    AvgHousePrice = []
    AvgPricePerFloor = []
    Longitude = []
    Latitude = []
    Colour = []
    Ziplist = []
    Pricelist = []
    Appearancelist = []
    AvgPricelist = []
    with open('USA Housing Dataset.csv', 'r') as f:
        #initialising csv reader
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            # Checking if the number of floors in a house is in the list or not then adding it to the relevant array element
            # and adding a 1 to the house number to be able to calcualte average
            if row[6] in HouseFloorNumber:
                # Finding the location of the match and setting it as a Location to be able to edit the other lists
                Location = HouseFloorNumber.index(row[6])
                HousePrice[Location] = float(HousePrice[Location]) + Price
                HouseFloorAppearance[Location] += 1
            #Adding the floor amount to the list if it has not appeared before and adding a entry into the price and 
            #Number in order for all 3 lists to have the same location for relevant information in the same location for easy editing
            else:
                HousePrice.append(row[1])
                HouseFloorNumber.append(row[6])
                HouseFloorAppearance.append(1)
            FullZip = row[16]
            Price = float(row[1])
            # Removing first 3 letters of the state zipcode
            Zip = FullZip[3:]
            if Zip in Ziplist:
                # Getting location of zipcode in list and adding new price+appearance onto the same index in the releveant lists
                Location = Ziplist.index(Zip)
                Appearancelist[Location] = int(Appearancelist[Location])+1
                Pricelist[Location] = int(Pricelist[Location])+Price
            else:
                # Adding the first instance for said zip and adding its price and an appearance to the lists
                Ziplist.append(Zip)
                Pricelist.append(int(Price))
                Appearancelist.append(int('1'))
                Coordinates = Country.query_postal_code(Zip)
                Longitude.append(Coordinates['longitude'])
                Latitude.append(Coordinates['latitude'])
    # Dividing Prices with amount of houses
    i=0
    for item in HousePrice:
        AvgHousePrice.append(HousePrice[i]/HouseFloorAppearance[i])
        AvgPricePerFloor.append(AvgHousePrice[i]/float(HouseFloorNumber[i]))
        i += 1
    print(HouseFloorNumber)
    print(AvgPricePerFloor)
    #sorting floor numbers while also keeping the price in the same location as the floor number
    HouseFloorNumber, AvgPricePerFloor = zip(*sorted(zip(HouseFloorNumber, AvgPricePerFloor)))
    print(HouseFloorNumber)
    print(AvgPricePerFloor)
    i=0
    #dividing all items in Price list with Apperance list to get the average house price for each zipcode
    for item in Appearancelist:
        AvgPricelist.append(Pricelist[i]/Appearancelist[i])
        i += 1
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
        i += 1
    x = Longitude
    y = Latitude
    # Making bar graph for Average floor price
    plt.bar (HouseFloorNumber, AvgPricePerFloor)
    plt.xlabel("Amount of floors")
    plt.ylabel("Price per floor")
    plt.xticks(HouseFloorNumber)
    plt.show()
    # Making scatter graph to show location and colour price of different zipcodes
    plt.scatter(x,y, c=Colour)
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()
    Menu()