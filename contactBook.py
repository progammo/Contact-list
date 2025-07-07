name_numbers = {}

print("You can save or delete phone numbers")
option = input("Do you want to save, delete or view a number S/D/V : ")

def reading():
    with open("F:\\Python learning\\projects\\contacts.txt","r") as f:
        print(f.read())

if option.lower() == "s":
    exit = False
    
    while exit == False:
        name = input("Enter name of contact number: ")

        while True:
            number = input("Enter contact number: ")

            if number.isdigit() and len(number) == 11:
                with open("F:\\Python learning\\projects\\contacts.txt","a") as f:
                    f.write(f"\n{name} : {number}")
                break
            else:
                print("Please enter a valid number\n")

        to_exit = input("Do you want to add another number Y/N: ")

        if to_exit.lower() == "y":
            continue
        elif to_exit.lower() == "n":
            exit = True
    
    reading()
    

elif option.lower() == "d":
    contact_delete = input("Enter contact name to be deleted: ")

    with open("F:\\Python learning\\projects\\contacts.txt", "r") as f:
        lines = f.readlines()

    with open("F:\\Python learning\\projects\\contacts.txt", "w") as f:
        for line in lines:
            if contact_delete.lower() not in line.lower():
                f.write(line)
    
    reading()

elif option.lower() == "v":
    reading()



