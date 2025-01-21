contact={}
def add_contact():
    print("\nYou can create a contact with Name,Phone Number,Email and Address for each person\n")
    name=input("Enter the name:")
    phone_no=input("Enter the phone number:")
    email=input("Enter the Email address:")
    address=input("Enter the address:")
    if name in contact:
        print("\nThis contact is already exist")
    else:
        contact[name]=[phone_no,email,address]
        print("\nContact added successfully")

def delete_contact():
    name=input("\nEnter the name to delete:")
    if name in contact:
        del contact[name]
        print("\nContact deleted successfully")
    else:
        print("\nThe name is doesnot exists in dictionary")           

def view_contact():
    if contact=={}:
        print("\nThe contact book is empty")
    else:
        for name in contact:
            print("\nName:",name)
            print("Phone Number:",contact[name][0])
            print("Email:",contact[name][1])
            print("Address:",contact[name][2])

def search_contact():
    name=input("\nEnter the name to search:")
    if name in contact:
        print("\nContact details Founded\n")
        print("Name:",name)
        print("Phone Number:",contact[name][0])
        print("Email:",contact[name][1])
        print("Address:",contact[name][2])
        
    else:
        print("\nThe contact is not founded")

def update_contact():
    
    if contact=={}:
        print("\nContact book is empty")

    else:
        name=input("\nEnter the Name to update:")    
        if name in contact:
            del contact[name]
            name=input("\nEnter the name:")
            phone_no=input("Enter the phone number:")
            email=input("Enter the Email address:")
            address=input("Enter the address:")
            contact[name]=[phone_no,email,address]
            print("\nContact updated successfully")

        else:
            print("\nName is not found")



    
print("Welcome to contact book\n")
while True:
    print("\n Contact Book\n1.Add Contact\n2.Delete Contact\n3.View Contact\n4.Search Contact\n5.Update Contact\n6.Exit\n")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            add_contact()
        case 2:
            delete_contact()
        case 3:
            view_contact()
        case 4:
            search_contact()
        case 5:
            update_contact()
        case 6:
            exit()
        case _:
            print("\nInvalid choice")
