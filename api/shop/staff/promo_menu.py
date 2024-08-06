import datetime

from api.models.promo_codes import PromoCode
from api.requests import promo_codes as promo_code_request
from api.dependencies.database import SessionLocal
def promo_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= PROMO CODE EDITOR ========")
            print("1. Create Promo Code")
            print("2. Modify Promo Code")
            print("3. Delete Promo Code")
            print("4. Show Active Promo Codes")
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
            create_promo_code()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            promo_code_request.show_all_promo_codes()
        valid_option_selected = 0

#QUESTION: CAN I CREATE AND MANAGE PROMOTIONAL CODES, INCLUDING SETTING EXPIRATION DATES?
#TODO: CREATE PROMO CODES, ADD PROMO API
def create_promo_code():
    creating_promo_code = 1
    while creating_promo_code == 1:
        name_accepted = 0
        while name_accepted == 0:
            name = input("Enter Name of New Promo Code (Exit/e to Cancel): ")
            if name.lower() == "exit" or name.lower() == "e":
                creating_promo_code = 0
                break
            elif name.replace(" ", "") == "":
                print("ERROR: Name cannot be blank")
            else:
                name_accepted = 1
        discount_accepted = 0
        if creating_promo_code == 1:
            while discount_accepted == 0:
                discount = input("Enter Discount %: ")
                if discount.replace(" ", "") == "":
                    print("ERROR: Discount cannot be blank")
                elif "." in discount:
                    try:
                        discount = float(discount)
                        promo_code_request.create(name, discount)
                        discount_accepted = 1
                    except:
                        print("ERROR: Invalid Input")
                else:
                    try:
                        discount = "."+discount
                        discount = float(discount)
                        promo_code_request.create(name, discount)
                        discount_accepted = 1
                    except:
                        print("ERROR: Invalid Input")

def delete_promo_code():
    with SessionLocal() as db:
        promo_code_request.show_all_promo_codes()
        name_accepted = 0
        exit = 0
        while name_accepted == 0:
            name = input("Enter Name of Promo Code to be Deleted (Exit/e to Cancel): ")
            if name.lower() == "exit" or name.lower() == "e":
                exit = 1
                break
            elif name.replace(" ", "") == "":
                print("ERROR: Name cannot be blank")
            else:
                deleted_promo_code = promo_code_request.delete(name.upper())
                if deleted_promo_code is None:
                    print("Unable to Delete Promo Code")
                else:
                    print("Promo Code Deleted!")

def modify_promo_code():
    with SessionLocal() as db:
        promo_code_request.show_all_promo_codes()
        name_accepted = 0
        exit = 0
        while name_accepted == 0:
            name = input("Enter Name of Promo Code to be Modified (Exit/e to Cancel): ")
            if name.lower() == "exit" or name.lower() == "e":
                exit = 1
                break
            elif name.replace(" ", "") == "":
                print("ERROR: Name cannot be blank")
            else:
                name = input("What do you want the new name to be?").strip()
                discount = input("Enter Discount %: ")
                if (float(discount) == Exception):
                    while not discount.isdigit():
                        print("Sorry, invalid number, please try again")
                        discount = input("Enter Discount %: ")
                discount = (1 - float(discount)) / 100
                expiration_date_str = input("Enter the expiration date (MM/DD/YYYY): ").strip()
                try:
                    expiration_date = datetime.datetime.strptime(expiration_date_str, "%m/%d/%Y").date()
                except ValueError:
                    print("ERROR: Invalid date format, please use MM/DD/YYYY.")
                    continue
                promo_code = promo_code_request.update(name.upper(), name, discount, expiration_date)
                if promo_code:
                    print("Promo Code Updated Successfully!")
                else:
                    print("Unable to update promo code.")
                name_accepted = True

delete_promo_code()