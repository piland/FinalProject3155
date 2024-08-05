from api.requests import accounts, order_details, orders, payment_information, reviews
from api.models.orders import Order
from api.controllers.orders import create as create_order
from api.models.order_details import OrderDetail
from api.controllers.order_details import create as create_order_detail
from api.models.payment_information import PaymentInformation
from api.controllers import payment_information as payment_information_controller, orders as order_controller, order_details as order_detail_controller
from api.requests.payment_information import update as payment_information_update
from api.db_interface import recipes, resources, roles, sandwiches
from api.shop.staff.resource_menu import resource_menu, show_all_resources
from api.shop.staff.sandwich_menu import sandwich_menu, show_all_sandwiches
from api.db_interface import recipes as recipes_db, resources as resources_db
from api.dependencies.database import SessionLocal
class Shop:
    def __init__(self):
        #If active_user_account remains None, account is guest
        self.active_user_account = None
        self.is_staff = False

    """========== STAFF MENU ============"""
    """=================================="""
    def staff_main_menu(self):
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
                    if option > -1 and option < 6:
                        valid_option_selected = 1
                except:
                    print("Invalid Option")

            #TODO: Reports, Recipes, Promos, the rest of Resources and Sandwiches
            if option == 0:
                exit = 1
            elif option == 1:
                pass
            elif option == 2:
                resource_menu()
            elif option == 3:
                sandwich_menu()
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            valid_option_selected = 0

    """STAFF FUNCTIONS"""
    """========================================================"""
    #QUESTION: HOW DOES THE SYSTEM ALERT ME IF THERE ARE INSUFFICIENT INGREDIENTS TO FULFILL AN ORDER?
    #TODO: SHOW WHEN THERE ARENT ENOUGH INGREDIENTS
    def is_enough_ingredients(self, recipe_id):
        pass

    #QUESTION: HOW CAN I VIEW THE LIST OF ALL ORDERS? IS THERE AN OPTION TO VIEW THE DETAILS OF A SPECIFIC ORDER?
    #TODO: VIEW ALL ORDERS
    def show_all_orders(self):
        pass

    #TODO: VIEW SINGLE ORDER DETAILS
    def show_order_details(self, order_id):
        pass

    #QUESTION: HOW CAN I IDENTIFY DISHES THAT ARE LESS POPULAR OR HAVE RECEIVED COMPLAINTS? IS THERE A WAY TO UNDERSTAND CUSTOMER DISATISFACTION?
    #TODO: VIEW UNPOPULAR ORDERS, ASK FOR THRESHOLD (eg. order constitutes 10% or less of sales or something)
    def show_unpopular_orders(self, threshold):
        pass

    #TODO: SHOW LOW-RATED ORDERS, ASK FOR THRESHOLD (eg. less than 2 stars)
    def show_low_rated_orders(self):
        pass

    #TODO: SHOW LOW-RATED ORDERS WITH DESCRIPTION
    def show_low_rated_orders_details(self):
        pass

    #QUESTION: CAN I CREATE AND MANAGE PROMOTIONAL CODES, INCLUDING SETTING EXPIRATION DATES?
    #TODO: CREATE PROMO CODES, ADD PROMO API
    def create_promo_code(self):
        pass

    #TODO: SHOW ALL ACTIVE PROMO CODES
    def show_active_promo_codes(self):
        pass

    #TODO: DELETE PROMO CODE
    def delete_promo_code(self, promo_code):
        pass

    #QUESTION: HOW CAN I DETERMINE THE TOTAL REVENUE GENERATED FROM FOOD SALES ON ANY GIVEN DAY?
    #TODO: SHOW TOTAL REVENUE
    def show_total_revenue(self, date):
        pass
        #TODO: sum orders totals on date

    #QUESTION: IS THERE A WAY TO VIEW THE LIST OF ORDERS WITHIN A SPECIFIC DATE RANGE?
    #TODO: LIST OF ORDER IN DATE RANGE
    def show_orders_between_dates(self, start_date, end_date):
        pass
        #TODO: filter order_list to show only between start_date and end_date

    """CUSTOMER FUNCTIONS"""
    """========================================================"""
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
                show_all_sandwiches()
            elif option == 2:
                self.place_order()
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            valid_option_selected = 0

    #QUESTION: HOW TO PLACE AN ORDER? I DO NOT WISH TO SIGN UP FOR AN ACCOUNT
    #TODO: ALERT WHEN ORDER CANNOT BE PROCESSED WHEN TRYING TO ORDER INSTEAD OF THE END
    def place_order(self):
        with SessionLocal() as db:
            cart = []
            placing_order = 1
            checkout = 0
            name_accepted = 0
            order_created = 0
            while placing_order == 1:
                while (placing_order == 1 and checkout == 0):
                    while name_accepted == 0:
                        customer_name = input("Input name on order (Exit/e to Cancel Order): ")
                        if customer_name.lower() == "exit" or customer_name.lower() == "e":
                            placing_order = 0
                            break
                        elif customer_name == "":
                            print("ERROR: Name Cannot be Blank")
                        else:
                            name_accepted = 1
                    if placing_order == 0:
                        break
                    if order_created == 0:
                        description = input("Order Notes (Allergies, Substitutions (Leave Blank to Skip): ")

                        print("===== ORDER TYPES =====")
                        print("1. Dine-In\n2. Takeout\n3. Delivery")
                        order_type_accepted = 0
                        while order_type_accepted == 0:
                            order_type = input("Enter order type ID: ")
                            try:
                                order_type = int(order_type)
                                if order_type < 1 or order_type > 3:
                                    print("ERROR: Invalid order type")
                                else:
                                    order_type_accepted = 1
                            except:
                                print("ERROR: Order type must be a number")
                        order_type = self.get_order_type(order_type)

                        order_data = {
                            "customer_name": customer_name,
                            "description": description,
                            "account_id": 1,
                            "order_type": order_type
                        }
                        order = Order(**order_data)
                        order_created = 1

                    show_all_sandwiches()
                    sandwich_id_accepted = 0
                    while sandwich_id_accepted == 0:
                        sandwich_id = input("Enter ID of sandwich to order (Exit/e to Cancel Order or Checkout/c to Checkout): ")
                        if sandwich_id.lower() == "exit" or sandwich_id.lower() == "e":
                            placing_order = 0
                            break
                        elif sandwich_id.lower() == "checkout" or sandwich_id.lower() == "c":
                            if len(cart) == 0:
                                print("Cart Empty! Please add items before checking out or type Exit/e to cancel")
                            else:
                                checkout = 1
                                break
                        try:
                            sandwich_id = int(sandwich_id)
                            sandwich_id_accepted = 1
                        except:
                            print("Sandwich ID must be an Integer and Exist on Menu")
                    if checkout == 1 or placing_order == 0:
                        break
                    sandwich = sandwiches.get_sandwich_by_id(sandwich_id)
                    sandwich_amount_accepted = 0
                    while sandwich_amount_accepted == 0:
                        sandwich_amount = input(f"Enter Number of {sandwich.sandwich_name}: ")
                        try:
                            sandwich_amount = int(sandwich_amount)
                            sandwich_amount_accepted = 1
                        except:
                            print("Sandwich Amount must be an Integer")

                    order_detail_data = {
                        "order_id": order.id,
                        "sandwich_id": sandwich_id,
                        "amount":  sandwich_amount
                    }

                    order_item = OrderDetail(**order_detail_data)
                    cart.append(order_item)

                """CHECKOUT"""
                order_total = 0
                for order_detail in cart:
                    sandwich_id = order_detail.sandwich_id
                    price = sandwiches.get_sandwich_by_id(sandwich_id).price
                    order_total += (price * order_detail.amount)

                payment_information_accepted = 0
                while payment_information_accepted == 0:
                    self.show_all_payment_information()
                    print(f"Your Total is {order_total}")
                    payment_id = input("Enter Payment Information ID (Exit/e to Cancel Transaction): ")
                    if payment_id.lower() == "exit" or payment_id.lower() == "e":
                        placing_order = 0
                        break
                    try:
                        payment_id = int(payment_id)
                        selected_payment_information = payment_information_controller.read_one(db, payment_id)
                        print(f"PAYMENT INFO BALANCE: {selected_payment_information.balance_on_account}")
                        if selected_payment_information.balance_on_account > order_total:
                            new_balance = float(selected_payment_information.balance_on_account) - float(order_total)
                            selected_payment_information.balance_on_account = new_balance
                            payment_information_update(payment_id, balance_on_account=new_balance)
                            print(f"PAYMENT ACCEPTED, NEW BALANCE ON ACCOUNT {payment_id}: ${new_balance}")
                            payment_information_accepted = 1
                    except Exception as e:
                        print(e)
                        print("ERROR: Payment ID must be Integer and Exist in Available Payment Options")
                total_recipe_dict = {}
                for item in cart:
                    recipe_dict = recipes_db.get_recipe_dict(item.sandwich_id)
                    multiplied_recipe_dict = {key: value * item.amount for key, value in recipe_dict.items()}
                    if not total_recipe_dict:
                        total_recipe_dict = multiplied_recipe_dict
                    else:
                        for key, value in multiplied_recipe_dict.items():
                            if key in total_recipe_dict:
                                total_recipe_dict[key] += value
                            else:
                                total_recipe_dict[key] = value
                resource_dict = resources_db.get_current_resource_dict()
                new_resource_dict = {key: resource_dict[key] - total_recipe_dict.get(key, 0) for key in resource_dict}
                has_negative_values = any(value < 0 for value in new_resource_dict.values())
                if has_negative_values:
                    print("Not Enough Resources to Process Order!")
                else:
                    for key, value in new_resource_dict.items():
                        resources_db.update_resource(key, amount = value)
                print("FOR TESTING PLEASE REMOVE LATER")
                print("NEW RESOURCE LIST")
                show_all_resources()
                if placing_order == 0:
                    break
                created_order = order_controller.create(db, order)
                for order_detail_item in cart:
                    order_detail_item.order_id = created_order.id
                    order_detail_controller.create(db, order_detail_item)
                placing_order = 0
                print("Finish!")

    def show_all_payment_information(self):
        with SessionLocal() as db:
            payment_information_list = payment_information_controller.read_all(db)
            print("===== PAYMENT INFORMATION =====")
            for payment_info in payment_information_list:
                print(payment_info)

    #QUESTION: HOW DO I PAY FOR ORDER?
    #TODO: AFTER CUSTOMER HAS ADDED DESIRED ITEMS TO ORDER, PROCESS TRANSACTION
    def process_payment(self):
        pass

    #TODO: THIS FUNCTION WILL ASK FOR INPUT REGARDING TYPE OF ORDER, MAY REMOVE IN FAVOR OF SIMPLER IMPLEMENTATION
    def get_order_type(self, input):
        type = "Dine-In"
        if input == 2:
            type = "Takeout"
        elif input == 3:
            type = "Delivery"
        return type

    #QUESTION: HOW CAN I TRACK THE STATUS OF MY ORDER BY MY TRACKING NUMBER?
    #TODO: GET ORDER STATUS FROM TRACKING NUMBER
    def check_order(self, tracking_number):
        pass

    #QUESTION: IS THERE A FEATURE THAT ALLOWS ME TO SEARCH FOR SPECIFIC TYPES OF FOOD?
    #TODO: IMPLEMENT SORTING FUNCTION FOR MENU ITEMS
    def get_filtered_menu(self, filter):
        pass

    #QUESTION: HOW CAN I RATE AND REVIEW DISHES I'VE ORDERED?
    #TODO: IMPLEMENT BOTH GET AND PUT REVIEW FUNCTIONS
    #TODO: DONT WE NEED TO SPECIFY WHAT ITEM WERE REVIEWING?
    def write_review(self, menu_item, stars, description):
        pass

    def get_reviews_for_single_item(self, menu_item):
        pass

    def get_menu_with_reviews(self):
        pass

    #QUESTION: HOW DO I APPLY A PROMOTIONAL CODE TO ME ORDER?
    #TODO: APPLY PROMOTIONAL CODE TO ORDER
    def apply_promo_code(self, code):
        pass

shop = Shop()
shop.customer_menu()