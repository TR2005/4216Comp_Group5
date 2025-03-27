import csv
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
def option_facts():
    print("You selected facts.")
def option_tomos():
    print("you selected user: Tomos")
    # place your visualisation code here please. @TR2005
def option_reece():
    print("you selected user: Reece")
    #
def option_oliver():
    print("you selected user: Oliver")
    # place your visualisation code here please. @oliver9362
def option_sam():
    print("you selected user: Sam")
    #place your visualisations code here sam
def main():
    while True:
        #main menu to be showed whenever the program opens 
        print(f"=== Main Menu ===\n1. Print Dataset\n2. Visualisations\n3. Facts\n4. Exit\n=================\nEnter your choice (1-4): ")
        choice = input()
        if choice == "1":
            option_print_dataset()
        elif choice == "2":
            option_visualisations()
        elif choice == "3":
            option_facts()
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
    