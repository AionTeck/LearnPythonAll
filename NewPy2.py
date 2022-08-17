import sys
users = {}


def createNewTable():
    id = 0
    while True:
        choise = int(
            input("What would you do with table? \n 1. Add new user \n 2. Read the table \n 3. Close the table\n"))
        match choise:
            case 1:
                name = str(input("Enter name of new user: "))
                users[id] = name
                id += 1
            case 2:
                print(users)
            case 3:
                print("File saving...")
                with open("fileTable.txt", "w") as f:
                    f.write(str(users))
                    f.close()
                sys.exit()

def editOldTable():
    choise = int(input("\n 1. Add new data \n 2. Edit existing data\n"))
    
    while True:

        match choise:
            case 1:
                with open("fileTable.txt", "a") as f:
