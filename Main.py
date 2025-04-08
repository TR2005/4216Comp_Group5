import csv
import matplotlib.pyplot as plt 
import pandas as pd 
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
    