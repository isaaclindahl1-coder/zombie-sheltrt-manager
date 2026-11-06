import json
from datetime import datetime


time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
        manger_input = input("Enter a option (1 thru 4)")
        if manger_input is 1:
            print("")
        elif manger_input is 2:
            print("")
        elif manger_input is 3:
            print("")
        elif manger_input is 4:
            print("")
            break
        else:
            print("Please try again")

menu()