import csv
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.patches as mpatches

def load_dataset():
    return pd.read_csv("USA Housing Dataset.csv")

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
    housing_prices = load_dataset()
    print("you selected user: Reece")
    #only getting the rows which have renovations 
    unsorted_renovated_true = housing_prices[housing_prices["yr_renovated"]>0]
    #sorting and removing dupes on the rows needed for the visualisation
    renovated_true_sorted = unsorted_renovated_true.sort_values(by="yr_renovated")
    renovated_true_nodupe = renovated_true_sorted.drop_duplicates("yr_renovated")
    #turning the sorted tables into individual lists with the needed rows for plotting 
    row_renovated_bef1970_price = renovated_true_nodupe["price"]
    row_renovated_bef1970 = renovated_true_nodupe["yr_renovated"]
    
    #plotting the first visualisation 
    fig, ax = plt.subplots()
    fig.suptitle("Price to year renovated", fontsize=16)
    ax.set_xlabel("Year renovated", fontsize=12)
    ax.set_ylabel("Price (Millions)", fontsize=12)
    ax.plot(row_renovated_bef1970, row_renovated_bef1970_price)
    ax.grid(True)
    plt.show()

#Set bar colour conditions for city prices visualisation
def bar_colour(price):
    if price <300000:
        return "green"
    elif price >=300000 and price < 800000:
        return "orange"
    else:
        return "red"
    
def oliver_visualisation1():
    data = load_dataset()
    print("you selected user: Oliver")
    
    #Group dataset by city
    data_grouped = data.groupby("city")["price"].mean()

    #Assign bars colours based on price
    colours = [bar_colour(p) for p in data_grouped]

    #Create the plot
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.bar(data_grouped.index, data_grouped, color = colours)
       
    green_patch = mpatches.Patch(color="green", label="Affordable Place To Live (average under $300000)")
    orange_patch = mpatches.Patch(color="orange", label="Average Cost Place To Live(average between $300000 and $800000")
    red_patch = mpatches.Patch(color="red", label="Expensive Place To Live(Over $800000)")

    ax.legend(handles=[green_patch, orange_patch,red_patch])

    #Labels and title
    ax.set_xlabel("City")
    ax.set_ylabel("Average Price ($)")
    ax.set_title("House Price Comparison Between Cities")

    #Rotate labels and add lines on y axis
    ax.set_xticklabels(data_grouped.index, rotation=90, fontsize = 9)
    ax.yaxis.grid(True)

    #Stop the graph using scientific notation
    plt.ticklabel_format(style = 'plain', axis = "y")

    #Make sure all labels are visible in the graph
    plt.tight_layout()

    #Show the graph
    plt.show()

def oliver_visualisation2():
    data = load_dataset()
    #Convert date column to correct format
    data["date"] = pd.to_datetime(data["date"])

    #Sort the dataset by date
    data = data.sort_values(by = "date")

    #Group the data by day and calculate average price
    data_grouped = data.groupby(data["date"].dt.date)["price"].mean()

    #Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data_grouped.index, data_grouped)

    #Labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.set_title("House Price Trends Over Time")

    #Stop the graph using scientific notation
    plt.ticklabel_format(style = 'plain', axis = "y")

    #Show the graph
    plt.grid(True)
    plt.show()

def option_oliver():
    print("You selected user: Oliver")
    while True:
        print(f"=== Oliver's Visualisations ===\n1. City Price Comparison\n2. Prices Over Time\n3. Return to previous menu")
        choice = input()

        if choice == "1":
            oliver_visualisation1()
        elif choice == "2":
            oliver_visualisation2
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 3.")

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