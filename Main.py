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
            print(f"")
        elif choice == "2":
          print(f"")
        elif choice == "3":
            print(f"")
        elif choice == "4":
            print(f"")
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

    duplicates = housing_prices_df['yr_renovated'][housing_prices_df['yr_renovated'].duplicated(keep=False)]
    avg_prices = housing_prices_df[housing_prices_df['yr_renovated'].isin(duplicates)].groupby('yr_renovated')['price'].mean()
    

    def replace_with_avg_price(product, price):
        if product in avg_prices:
            return avg_prices[product]
        else:
            return price
    
    housing_prices_df['price'] = housing_prices_df.apply(lambda row: replace_with_avg_price(row['yr_renovated'], row['price']), axis=1)
    housing_prices_df.sort_values(by='yr_renovated')
    ren_housing_prices = housing_prices_df.sort_values(by='yr_renovated')[housing_prices_df.sort_values(by='yr_renovated')["yr_renovated"]>0]
    price_housing_prices = ren_housing_prices["price"]
    yrren_housing_prices = ren_housing_prices["yr_renovated"]

    #plotting the first visualisation 
    fig, ax = plt.subplots()
    fig.suptitle("Price to year renovated", fontsize=16)
    ax.set_xlabel("Year renovated", fontsize=12)
    ax.set_ylabel("Price (Millions)", fontsize=12)
    ax.plot(yrren_housing_prices,price_housing_prices)
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
    