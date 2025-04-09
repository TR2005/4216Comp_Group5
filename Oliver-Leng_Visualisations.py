import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd 

#Function to read the dataset so each visualisation can call it and assign it to a variable
def load_dataset():
    return pd.read_csv("USA Housing Dataset.csv")#
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
    
    #Group dataset by city and find the mean
    data_grouped = data.groupby("city")["price"].mean()

    #Assign bars colours based on price
    colours = [bar_colour(p) for p in data_grouped]

    #Create the plot
    fig, ax = plt.subplots(figsize = (13, 6))
    ax.bar(data_grouped.index, data_grouped, color = colours)
       
    #Create different legend patches for the different prices
    green_patch = mpatches.Patch(color="green", label="Affordable Place To Live (average under $300000)")
    #r means the label is a raw string so no syntax error for escape character
    orange_patch = mpatches.Patch(color="orange", label=r"Average Cost Place To Live (average between \$300000 and \$800000)")
    red_patch = mpatches.Patch(color="red", label="Expensive Place To Live (Average over $800000)")

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

    while True:
        print(f" === House Price Trend Options === \n1. View overall house price change over time\n2. Compare house prices over time between 2 ZIP codes\n3. Return to previous menu")
        choice = input()

        if choice == "1":
            #Sort the dataset by date
            data = data.sort_values(by = "date")

            #Group the data by day and calculate average price
            data_grouped = data.groupby(data["date"].dt.date)["price"].mean()

            #Create the plot
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(data_grouped.index, data_grouped)

             #Labels and title
            ax.set_xlabel("Date")
            ax.set_ylabel("Average Price ($)")
            ax.set_title("House Price Trends Over Time")

            #Stop the graph using scientific notation
            plt.ticklabel_format(style = 'plain', axis = "y")

            #Show the graph
            plt.grid(True)
            plt.show()

        elif choice == "2":
            zip1 = input("Enter the first ZIP code: ")
            zip2 = input("Enter the second ZIP code: ")

            #Filters the dataset to only have the right statezip in the variables
            zip1_data = data[data["statezip"] == zip1]
            zip2_data = data[data["statezip"] == zip2]

            #Groups the data by date to get an average price for each zip
            zip1_grouped = zip1_data.groupby(zip1_data["date"].dt.date)["price"].mean()
            zip2_grouped = zip2_data.groupby(zip2_data["date"].dt.date)["price"].mean()

            #Create the plots
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(zip1_grouped.index, zip1_grouped, label=zip1)
            ax.plot(zip2_grouped.index, zip2_grouped, label=zip2)

            #Labels and title
            ax.set_xlabel("Date")
            ax.set_ylabel("Average Price ($)")
            ax.set_title("House Price Trends Over Time: " +zip1+ " vs " +zip2)
            ax.legend()

            #Stop the graph using scientific notation
            plt.ticklabel_format(style = 'plain', axis = "y")

            #Show the graph
            plt.grid(True)
            plt.show()

        elif choice == "3":
            break

        else:
            print("Invalid choice, please choose a number between 1 and 3")

#Menu to allow user to select which visualisation to see
def option_oliver():
    while True:
        print(f"=== Oliver's Visualisations ===\n1. City Price Comparison\n2. Prices Over Time\n3. Exit")
        choice = input()

        if choice == "1":
            oliver_visualisation1()
        elif choice == "2":
            oliver_visualisation2()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 3.")

option_oliver()