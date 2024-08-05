from api.shop.staff.resource_menu import resource_menu
from api.shop.staff.sandwich_menu import sandwich_menu
from api.shop.staff.report_menu import report_menu
from api.shop.staff.promo_menu import promo_menu
from api.shop.customer import customer_options

class Shop:
    def __init__(self, account_id):
        self.account_id = account_id

    """========== STAFF MENU ============"""
    """=================================="""
    def staff_menu(self):
        exit = 0
        valid_option_selected = 0
        while exit != 1:
            while valid_option_selected != 1:
                option = -1
                print("\n======= BACK OF HOUSE OPTIONS ========")
                print("1. Reports")
                print("2. Resources")
                print("3. Sandwiches")
                print("4. Recipes")
                print("5. Orders")
                print("6. Promos")
                print("0. Shut Down")

                try:
                    option = int(input("\nEnter One of the Options Above: "))
                    if option > -1 and option < 7:
                        valid_option_selected = 1
                except:
                    print("Invalid Option")

            #TODO: Reports, Recipes, Promos, the rest of Resources and Sandwiches
            if option == 0:
                exit = 1
            elif option == 1:
                report_menu()
            elif option == 2:
                resource_menu()
            elif option == 3:
                sandwich_menu()
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                promo_menu()
            valid_option_selected = 0

    def customer_menu(self):
        exit = 0
        valid_option_selected = 0
        while exit != 1:
            while valid_option_selected != 1:
                option = -1
                print("\n======= WELCOME TO JETHANASI'S! ========")
                print("1. View Menu")
                print("2. Place Order")
                print("3. Check Order Status")
                print("4. Write Review")
                print("5. See Reviews")
                print("0. Exit")

                try:
                    option = int(input("\nEnter One of the Options Above: "))
                    if option > -1 and option < 6:
                        valid_option_selected = 1
                except:
                    print("Invalid Option")

            # TODO: Reports, Recipes, Promos, the rest of Resources and Sandwiches
            if option == 0:
                exit = 1
            elif option == 1:
                customer_options.show_menu()
            elif option == 2:
                customer_options.place_order()
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            valid_option_selected = 0

shop = Shop()
shop.staff_menu()