import os

#function adds a contact to the function
def add():
    list = []
    valid = False
    file = open('contacts.txt', 'a')
    name = input("Enter the contact's name: ")
    list.append(name)
    address = input("Enter the contact's address: ")
    list.append(address)
    while valid == False:
        try:
            number = float(input("Enter the contact's phone number (no dashes): "))
            list.append(str(number))
            valid = True
        except:
            print("Please only enter numbers.")

    email = input("Enter the contact's email: ")
    list.append(email)

    file.write(str(name) + "\n")            #adds each item to the addressbook
    file.write(str(address) + "\n")
    file.write(str(number) + "\n")
    file.write(str(email) + "\n")

    file.close()
    print("Your contact has been successfully added.")

    main()


#function prints entire address book
def printbook():
    file = open('contacts.txt', 'r')
    list = file.readlines()
    for index in list:
        print(index.strip())

    file.close()

    main()
#function searches for a specific contact
def search():
    file = open('contacts.txt', 'r')
    list = file.readlines()
    search = input("What is the name of the contact you are searching for?: ")

    notfound = True
    for i in list:
        if i.__contains__(search):
            value = list.index(search + '\n')
            print(list[value].strip())
            print(list[value + 1].strip())
            print(list[value + 2].strip())
            print(list[value + 3].strip())
            notfound = False

    if notfound == True:
        print("There is no contact with that name in your addressbook.")

    file.close()
                              #returns back to menu
    main()

#function makes any changes to a specific contact
def modify():

    file = open('contacts.txt', 'r')
    list = file.readlines()
    for i in list:
        print(i.strip())
    contact = input("Which contact would you like to modify? ")

    for i in list:
        if i.__contains__(contact):
            found = True
            oldname = list.index(contact + '\n')
    try:
        if found == True:
            modify = input("What would you like to change (name, address, phone number, or email)?: ")

            if modify == "name":
                newname = input("What is the new name of the contact?: ")
                list[oldname] = newname + "\n"

                temp = open('tempfile.txt', 'w')

                temp.writelines(list)

                os.remove('contacts.txt')
                os.rename('tempfile.txt', 'contacts.txt')
                temp.close()
                file.close()
                print("The name has successfully been changed.")
                main()

            elif modify == "address":
                newaddress = input("What is the new address of the contact?: ")
                oldaddress = oldname + 1

                list[oldaddress] = newaddress + '\n'
                temp = open('tempfile.txt', 'w')

                temp.writelines(list)

                os.remove('contacts.txt')
                os.rename('tempfile.txt', 'contacts.txt')
                temp.close()
                file.close()
                print("The address has successfully been changed.")
                main()
            elif modify == "phone number":
                newnumber = input("What is the new phone number of the contact?: ")
                oldnumber = oldname + 2

                list[oldnumber] = newnumber + '\n'
                temp = open('tempfile.txt', 'w')

                temp.writelines(list)

                os.remove('contacts.txt')
                os.rename('tempfile.txt', 'contacts.txt')
                temp.close()
                file.close()
                print("The phone number has successfully been changed.")
                main()

            elif modify == "email":
                newemail = input("What is the new email of the contact?: ")
                oldemail = oldname + 3

                list[oldemail] = newemail + '\n'
                temp = open('tempfile.txt', 'w')

                temp.writelines(list)

                os.remove('contacts.txt')
                os.rename('tempfile.txt', 'contacts.txt')
                temp.close()
                file.close()
                print("The email has successfully been changed.")
                continueprogram = input("Do you want to continue (y/n)?: ")
                main()

            else:
                print("That is an invalid choice.")
                file.close()

                continueprogram = input("Do you want to continue (y/n)?: ")
                main()


    except:         #if no contact found in addressbook
        print("There is no contact with that name in your addressbook.")
        file.close()

    finally:                #returns to menu
        main()


#function deletes entire specific contact
def deletecontact():
    file = open('contacts.txt', 'r')
    list = file.readlines()
    for i in list:
        print(i.strip())
    contact = input("Which contact would you like to delete? ")
    found = False

    for i in list:
        if i.__contains__(contact):
            deletename = list.index(contact + '\n')

            for i in range(4):
                list.remove(list[deletename])

            temp = open('tempfile.txt', 'w')
            temp.writelines(list)

            os.remove('contacts.txt')
            os.rename('tempfile.txt', 'contacts.txt')
            temp.close()
            file.close()
            print("The contact has successfully been deleted.")
            found = True

    if found == False:
        print("That contact could not be found in your addressbook.")

    #returns back to menu
    main()


def main():

    print("1. Add new contact")
    print("2. Print entire address book")
    print("3. Search for a contact")
    print("4. Modify information about a specific contact")
    print("5. Delete a contact")
    print("6. Exit")

    choice = float(input("Select an option 1-6: "))

    while choice < 1 or choice > 6:
        print("That is not a valid choice.")
        choice = float(input("Please select an option 1-6: "))

    if choice == 1:
        add()
    if choice == 2:
        printbook()
    if choice == 3:
        search()
    if choice == 4:
        modify()
    if choice == 5:
        deletecontact()
    if choice == 6:
        exit(0)

main()
