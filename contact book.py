contact ={}


def display_contact():
    print(contact.items())
    print("Name \t\t Contact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input(" 1. Add new Contact\n2. Search Contact \n3. Display contact\n 4. Edit Contact\n 5.Delete contact \n 6.exitt\n enter your choice "))
    if choice == 1:
        name = input("Enter contact name")
        phone = input("Enter the Mobile Number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name")
        if search_name in contact:
            print(search_name,"'s Contact Number is ",contact[Search_name])
        else:
            print("name not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter contact to be edited")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("contact not found in contact book")
    elif choice == 5:
        del_contact = input("enter contact to be deleted")
        if del_contact in contact:
            comfirm = input("do you want to delete this contact y/n?")
            if comfirm == 'y' or comfirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("name is not found in contact book")
    else:
        break

