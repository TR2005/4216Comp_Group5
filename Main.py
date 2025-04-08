import csv
import pgeocode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import pandas as pd 
print('This is main.py')
def option_print_dataset():
    print("You selected Print Dataset.")
    #runs through the dataset and prints it
    with open('USA Housing Dataset.csv', 'r') as f: 
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)
        next(csv_reader)
        for row in csv_reader:
            print(row)
def option_visualisations():
    print("You selected Visualisations.")
    user_selection()
def option_questions():
    print("You selected questions\n Please enter a user")
    while True: 
        print(f" === Select a user. === \n1. Tomos\n2. Reece\n3. Oliver\n4. Sam\n5. Return to main  menu\n================\nEnter your choice (1-5): ")
        choice = input()
        if choice == "1": 
            print(f"-Using Pgeocode to convert zipcode to lattitude longitude and using average house prices for said post code to generate a map with different coloured dots to display where houses are most expensive (using column B and Q)\n -Comparing the price differences in the houses that are waterfront with those that arent")
        elif choice == "2":
          print(f"-Comparison between the price of a house and whether its renovated/what date it was renovated \n-how the ammount of bathrooms affects the price of the house and what the average price of 1 bathroom is")
        elif choice == "3":
            print(f"-comparison between the condition of the house and what year it was built and wether it needed renevating or not and how that corrilates to the condition.\n-comparioson between the total sqft and how that corrilates to the number of rooms and the price of the property.")
        elif choice == "4":
            print(f"-Comparing house prices over time\n-Comparing house prices between different cities")
        elif choice == "5":
            main()
        else:
            print("Invalid choice, please choose a number between 1 and 5.")



def option_tomos():
    print("you selected user: Tomos")
    # place your visualisation code here please. @TR2005
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
    #sorting floor numbers while also keeping the price in the same location as the floor number
    HouseFloorNumber, AvgPricePerFloor = zip(*sorted(zip(HouseFloorNumber, AvgPricePerFloor)))
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
    green = mpatches.Patch(color='green', label='<200k')
    red = mpatches.Patch(color='red', label='200k-400k')
    blue = mpatches.Patch(color='blue', label='400k-600k')
    purple= mpatches.Patch(color='purple', label='600k-800k')
    pink= mpatches.Patch(color='pink', label='800k-1000k')
    orange= mpatches.Patch(color='orange', label='1000k-1200k')
    brown= mpatches.Patch(color='brown', label='1200k-1400k')
    gray= mpatches.Patch(color='gray', label='1400k-1600k')
    olive= mpatches.Patch(color='olive', label='1600k-1800k')
    cyan= mpatches.Patch(color='cyan', label='1800k-2000k')
    black= mpatches.Patch(color='black', label='2000k+')
    # Making bar graph for Average floor price
    plt.bar (HouseFloorNumber, AvgPricePerFloor)
    plt.xlabel("Amount of floors")
    plt.ylabel("Price per floor")
    plt.xticks(HouseFloorNumber)
    plt.show()
    # Making scatter graph to show location and colour price of different zipcodes
    x = Longitude
    y = Latitude
    #Making spaceing for the graph so that each point is shown cleary within it 
    #(Image requires a extent otherwise it resizes the graph to start at 0 and strech it to its resolution)
    LongitudeSpacing = float(max(Longitude)-min(Longitude))*0.05
    LatitudeSpacing = float(max(Latitude)-min(Latitude))*0.05
    ImageAreaXMin = min(Longitude) - LongitudeSpacing
    ImageAreaXMax = max(Longitude) + LongitudeSpacing
    ImageAreaYMin = min(Latitude) - LatitudeSpacing
    ImageAreaYMax = max(Latitude) + LatitudeSpacing
    Image1 = mpimg.imread('Area image.png')
    plt.imshow(Image1, extent=[ImageAreaXMin, ImageAreaXMax, ImageAreaYMin, ImageAreaYMax])
    plt.scatter(x,y, c=Colour)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=4, handles=[green, red, blue, purple, pink, orange, brown, gray, olive, cyan, black])
    plt.show()
def option_reece():
    print("you selected user: Reece")
    housing_prices = pd.read_csv("USA Housing Dataset.csv")
    housing_prices_df = pd.DataFrame(housing_prices)
    #determine duplicates and also their respective averages 
    bath_duplicates = housing_prices_df['bathrooms'][housing_prices_df['bathrooms'].duplicated(keep=False)]
    duplicates = housing_prices_df['yr_renovated'][housing_prices_df['yr_renovated'].duplicated(keep=False)]
    bath_avg_prices = housing_prices_df[housing_prices_df['bathrooms'].isin(bath_duplicates)].groupby('bathrooms')['price'].mean()
    avg_prices = housing_prices_df[housing_prices_df['yr_renovated'].isin(duplicates)].groupby('yr_renovated')['price'].mean()
    #define both methods of replacing the duplicated rows
    def replace_with_avg_price(product, price):
        if product in avg_prices:
            return avg_prices[product]
        else:
            return price 
    def replace_with_bath_avg_price(product, price):
        if product in bath_avg_prices:
            return bath_avg_prices[product]
        else:
            return price
    #using the previous functions to put the averages back into the correct rows and then getting the needed data out of the datafrane
    housing_prices_df['price'] = housing_prices_df.apply(lambda row: replace_with_avg_price(row['yr_renovated'], row['price']), axis=1)
    housing_prices_df.sort_values(by='yr_renovated')
    ren_housing_prices = housing_prices_df.sort_values(by='yr_renovated')[housing_prices_df.sort_values(by='yr_renovated')["yr_renovated"]>0]
    price_housing_prices = ren_housing_prices["price"]
    yrren_housing_prices = ren_housing_prices["yr_renovated"]
    #same as previous block but for the other visualisation data 
    housing_prices_df['price'] = housing_prices_df.apply(lambda row: replace_with_bath_avg_price(row['bathrooms'], row['price']), axis=1)
    housing_prices_df.sort_values(by='bathrooms')
    bath_housing_prices = housing_prices_df.sort_values(by='bathrooms')[housing_prices_df.sort_values(by='bathrooms')["bathrooms"]>0]
    bath_price = bath_housing_prices["price"]
    bathrooms_housing_prices = bath_housing_prices["bathrooms"]
    #plotting the first visualisation 
    fig, ax = plt.subplots()
    fig.suptitle("Price to year renovated", fontsize=16)
    ax.set_xlabel("Year renovated", fontsize=12)
    ax.set_ylabel("Price (Millions)", fontsize=12)
    ax.plot(yrren_housing_prices,price_housing_prices)
    ax.grid(True)
    plt.show()
    #plotting the second visualisation 
    fig, ax = plt.subplots()
    fig.suptitle("Price to bathrooms", fontsize=16)
    ax.set_xlabel("Bathrooms", fontsize=12)
    ax.set_ylabel("Price (Millions)", fontsize=12)
    ax.plot(bathrooms_housing_prices, bath_price)
    ax.grid(True)
    plt.show()


def option_oliver():
    print("you selected user: Oliver")
    # place your visualisation code here please. @oliver9362
def option_sam():
    print("you selected user: Sam")
    #place your visualisations code here sam
def main():
    while True:
        #main menu to be showed whenever the program opens 
        print(f"=== Main Menu ===\n1. Print Dataset\n2. Visualisations\n3. Questions\n4. Exit\n=================\nEnter your choice (1-4): ")
        choice = input()
        if choice == "1":
            option_print_dataset()
        elif choice == "2":
            option_visualisations()
        elif choice == "3":
            option_questions()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 4.")
def user_selection():
     while True: 
        print(f" === Select a user. === \n1. Tomos\n2. Reece\n3. Oliver\n4. Sam\n5. Return to main  menu\n================\nEnter your choice (1-5): ")
        choice = input()
        if choice == "1": 
            option_tomos()
        elif choice == "2":
            option_reece()
        elif choice == "3":
            option_oliver()
        elif choice == "4":
            option_sam()
        elif choice == "5":
            main()
        else:
            print("Invalid choice, please choose a number between 1 and 5.")
main()