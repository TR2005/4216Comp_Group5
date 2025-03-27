import csv
with open('USA Housing Dataset.csv', 'r') as f:



        def print_menu():
            #main menu to be showed whenever the program opens 
            print("=== Main Menu ===")
            print("1. Print Dataset")
            print("2. Visualisations")
            print("3. Facts")
            print("4. Exit")
            print("================")

        def print_user():
            #menu for user to be selected
            print(" === Select a user. === ")
            print("1. Tomos")
            print("2. Reece")
            print("3. Oliver")
            print("4. Sam")
            print("5. cancel")
            print("================")

        def option_print_dataset():
            print("You selected Print Dataset.")
            #runs through the dataset and prints it 
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
                print_menu()
                try:
                    choice = int(input("Enter your choice (1-4): "))
                    if choice == 1:
                        option_print_dataset()
                    elif choice == 2:
                        option_visualisations()
                    elif choice == 3:
                        option_facts()
                    elif choice == 4:
                        print("Exiting the program...")
                        break
                    else:
                        print("Invalid choice, please choose a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        def user_selection():
             while True: 
                print_user()
                try:
                    choice = int(input("Enter your choice (1-4): "))
                    if choice == 1: 
                        option_tomos()
                    elif choice == 2:
                        option_reece()
                    elif choice == 3:
                        option_oliver()
                    elif choice == 4:
                        option_sam()
                    elif choice == 5:
                        print("cancelling operation...")
                        break
                    else:
                        print("Invalid choice, please choose a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()