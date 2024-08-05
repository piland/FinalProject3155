def recipe_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= PROMO CODE EDITOR ========")
            print("1. Create Promo Code")
            print("2. Modify Promo Code")
            print("3. Delete Promo Code")
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
            pass
        valid_option_selected = 0

#QUESTION: CAN I CREATE AND MANAGE PROMOTIONAL CODES, INCLUDING SETTING EXPIRATION DATES?
#TODO: CREATE PROMO CODES, ADD PROMO API
def create_promo_code():
    pass

#TODO: SHOW ALL ACTIVE PROMO CODES
def show_active_promo_codes():
    pass

#TODO: DELETE PROMO CODE
def delete_promo_code():
    pass