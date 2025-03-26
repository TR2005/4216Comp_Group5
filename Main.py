import csv
def Menu():
    print(f"Please input whos part of the project you wish to run\n1.Reece\n2.Tomos\n3.Oliver\n4.Sam")
    Selection = int(input())
    print(Selection)
    if Selection == 1:
        Reece()
    elif Selection == 2:
        print("Tomos")
        Tomos()
        print("Tomos")
    elif Selection == "3":
        Oliver()
    elif Selection == "4":
        Sam()
    else:
        print("incorrect input please try again")
        Menu()
Menu()
with open('USA Housing Dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        i=0