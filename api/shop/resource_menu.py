from api.db_interface import resources

def resource_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= RESOURCE EDITOR ========")
            print("1. Add New Resource")
            print("2. Restock Resource")
            print("3. Subtract Resource")
            print("4. Delete Resource")
            print("5. Show All Resources")
            print("6. Update Resource")
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
            add_new_resource()
        elif option == 2:
            add_resource()
        elif option == 3:
            subtract_resource()
        elif option == 4:
            delete_resource()
        elif option == 5:
            show_all_resources()
        elif option == 6:
            update_resource()
        valid_option_selected = 0

def add_new_resource():
    name_accepted = False
    while name_accepted == False:
        name = input("Input the Name of the New Resource: ")
        if name == "":
            print("ERROR: Name Cannot be Blank\n")
        else:
            name_accepted = True
    starting_amount_accepted = False
    while starting_amount_accepted == False:
        starting_amount = input("Input the Starting Amount of the New Resource: ")
        try:
            starting_amount = int(starting_amount)
            starting_amount_accepted = True
        except:
            print("ERROR: Amount Must be Integer\n")
    resources.create_resource(name, starting_amount)
    print(
        f"\n==================================\nADDED RESOURCE {name} WITH STARTING AMOUNT {starting_amount}\n==================================")


def add_resource():
    if len(resources.get_all_resources()) == 0:
        print("Resource List Empty!")
    else:
        show_all_resources()
        id_accepted = False
        cancel = False
        while id_accepted == False:
            id = input("Enter the ID of the Resource to Restock (Cancel/c to Cancel): ")
            if id.lower() == "cancel" or id.lower() == "c":
                cancel = True
                break
            try:
                id = int(id)
                db_entry_amount = resources.get_resource_by_id(id).amount
            except:
                print("ID must be an Integer and Exist in Resources")
        if cancel == True:
            print("Cancelling Operation")
        else:
            amount = int(input("Enter the Amount to Add: "))
            new_value = db_entry_amount + amount
            resources.update_resource(id, amount=new_value)


def subtract_resource():
    show_all_resources()
    id_accepted = False
    cancel = False
    while id_accepted == False:
        id = input("Enter the ID of the Resource to be Subtracted (Cancel/c to Cancel): ")
        if id.lower() == "cancel" or id.lower() == "c":
            cancel = True
            break
        try:
            id = int(id)
            db_entry_amount = resources.get_resource_by_id(id).amount
            print(resources.get_resource_by_id(id))
        except:
            print("ID must be an Integer and Exist in Resources")
    if cancel == True:
        print("Cancelling Operation")
    else:
        amount = int(input("Enter the Amount to Subtract: "))
        new_value = db_entry_amount - amount
        if new_value < 0:
            print("ERROR: Resource Amounts Cannot be Negative, Aborting Attempt...")
        else:
            resources.update_resource(id, amount=new_value)


def show_all_resources():
    resource_list = resources.get_all_resources()
    print("\n========== RESOURCE LIST ==========")
    for resource in resource_list:
        print(resource)
    print("===================================")


def update_resource():
    show_all_resources()
    id = int(input("Enter ID of Resource to be Updated: "))
    name = input("Enter New Name of Resource (Leave Blank to Skip): ")
    amount_accepted = False
    while amount_accepted == False:
        amount = input("Enter New amount of Resource (Leave Blank to Skip): ")
        if name == "":
            name = None
        if amount == "":
            amount = None
        else:
            try:
                amount = int(amount)
                amount_accepted = True
            except:
                print("Invalid Input, Only Numbers and Decimals Allowed for amount")
    resources.update_resource(id, name, amount)


def delete_resource():
    show_all_resources()
    id = int(input("Enter the ID of the Resource to be Deleted: "))
    resource_deleted = resources.delete_resource(id)
    if resource_deleted:
        print(f"Resource ID {id} Deleted")
    else:
        print(f"Unable to Delete Resource ID {id}")