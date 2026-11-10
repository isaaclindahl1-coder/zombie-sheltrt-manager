import json
from datetime import datetime

def test_for_file():
    try:
        with open("shelter.json", "r", encoding="utf-8") as file:
            shelter_text = file.read()
            return True
    except FileNotFoundError:
        print("The json file is missing")
        return False


def shelter():   
    with open("shelter.json", "r") as file:
        info = json.load(file)
        return info
    
shelter_data = shelter()

time_stamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
entry = f"{time_stamp} | Finished Chapter 3"

with open("reading_journal.log", "a", encoding="utf-8") as file:
    file.write(entry + "\n")


try:
    with open("reading_journal.log", "r", encoding="utf-8") as file:
        journal_text = file.read()
    if journal_text.strip():
        print(journal_text)
    else:
        print("The reading the journal is empty.")
except FileNotFoundError:
    print("No reading journal entries have been saved yet.")

def menu():
    while True:
        print("Zombie Shelter Manager:")
        print("1. Veiw shelter information")
        print("2. Change a shelter value")
        print("3. Veiw change log")
        print("4. Quit")
        manger_input = input("Enter a option (1 thru 4): ")
        if manger_input == "1":
            print("Veiwing shelter infromation")
        elif manger_input == "2":
            print("Changing shelter value")
        elif manger_input == "3":
            print("Veiwing change log")
        elif manger_input == "4":
            print("Thank you for managing the shelter!")
            return
        else:
            print("Please try again")

loop = test_for_file()
while loop != False:
    menu()

def shelter_values():
    for thing, data in shelter:
        