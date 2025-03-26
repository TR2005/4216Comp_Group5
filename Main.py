import csv
def Menu():
    i=0
    Selection = ""
    while i == 0:
        print(f"Please input whos part of the project you wish to run\n1.Reece\n2.Tomos\n3.Oliver\n4.Sam")
        Selection = input()
        if Selection == "1":
            i=1
            Reece()
        elif Selection == "2":
            i=1
            Tomos()
        elif Selection == "3":
            i=1
            Oliver()
        elif Selection == "4":
            i=1
            Sam()
        else:
            print("incorrect input please try again")
#Executing menu code block
Menu()
with open('USA Housing Dataset.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        i=0