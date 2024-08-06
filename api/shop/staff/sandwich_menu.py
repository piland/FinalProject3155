from api.db_interface import sandwiches

def sandwich_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= SANDWICH EDITOR ========")
            print("1. Add New Sandwich")
            print("2. Delete Sandwich")
            print("3. Show All Sandwiches")
            print("4. Update Sandwich")
            print("0. Exit to Main Menu")

            try:
                option = int(input("\nEnter One of the Options Above: "))
                if option > -1 and option < 7:
                    valid_option_selected = 1
            except:
                print("Invalid Option")

        if option == 0:
            exit = 1
        elif option == 1:
            add_new_sandwich()
        elif option == 2:
            remove_sandwich()
        elif option == 3:
            sandwiches.show_all_sandwiches()
        elif option == 4:
            update_sandwich()
        valid_option_selected = 0

def add_new_sandwich():
    sandwich_name_accepted = False
    while sandwich_name_accepted == False:
        sandwich_name = input("Enter Name of New Sandwich: ")
        if sandwich_name != "":
            sandwich_name_accepted = True
        else:
            print("\nERROR: Sandwich Name Cannot be Blank\n")
    price_accepted = False
    while price_accepted == False:
        price = input("Enter New Price of Sandwich: ")
        try:
            price = float(price)
            price_accepted = True
        except:
            print("\nERROR: Invalid Input, Only Numbers and Decimals Allowed for Price\n")
    tags = ""
    sandwiches.create_sandwich(sandwich_name, price, tags)
    print(f"\n==================================\nADDED SANDWICH {sandwich_name} WITH PRICE ${price}\n==================================")

def remove_sandwich():
    sandwiches.show_all_sandwiches()
    id = int(input("Enter ID of Sandwich to be Removed: "))
    sandwich_deleted = sandwiches.delete_sandwich(id)
    if sandwich_deleted:
        print(f"Sandwich ID {id} Deleted")
    else:
        print("Unable to Delete Sandwich")

def update_sandwich():
    sandwiches.show_all_sandwiches()
    id = int(input("Enter ID of Sandwich to be Updated: "))
    name = input("Enter New Name of Sandwich (Leave Blank to Skip): ")
    price_accepted = False
    while price_accepted == False:
        price = input("Enter New Price of Sandwich (Leave Blank to Skip): ")
        if name == "":
            name = None
        if price == "":
            price = None
        else:
            try:
                price = float(price)
                price_accepted = True
            except:
                print("Invalid Input, Only Numbers and Decimals Allowed for Price")
    tags = ""
    sandwiches.update_sandwich(id, name, price, tags)
    print(f"\nSANDWICH ID {id} UPDATED, NAME: {sandwiches.get_sandwich_by_id(id).sandwich_name}, PRICE: {sandwiches.get_sandwich_by_id(id).price}")