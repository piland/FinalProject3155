from api.requests import accounts, order_details, orders, paymentInformation, reviews
from api.db_interface import recipes, resources, roles, sandwiches
from api.shop.resource_menu import resource_menu
from api.shop.sandwich_menu import sandwich_menu
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
                print("======= BACK OF HOUSE OPTIONS ========")
                print("1. Reports")
                print("2. Resources")
                print("3. Sandwiches")
                print("4. Recipes")
                print("5. Promos")
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
        pass

    #QUESTION: HOW TO PLACE AN ORDER? I DO NOT WISH TO SIGN UP FOR AN ACCOUNT
    #TODO: ADD MENU ITEMS TO ORDER TO BE PROCESSED WHEN ORDER IS PLACED, ACCOUNT NOT NEEDED
    def place_order(self):
        #order_type() somewhere in here
        #process_payment() somewhere in here
        pass

    #QUESTION: HOW DO I PAY FOR ORDER?
    #TODO: AFTER CUSTOMER HAS ADDED DESIRED ITEMS TO ORDER, PROCESS TRANSACTION
    def process_payment(self):
        pass

    #QUESTION: DOES THE SYSTEM SUPPORT DIFFERENT TYPES OF ORDERING
    #TODO: THIS FUNCTION WILL ASK FOR INPUT REGARDING TYPE OF ORDER, MAY REMOVE IN FAVOR OF SIMPLER IMPLEMENTATION
    def order_type(self):
        #return order_type
        pass

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
shop.staff_main_menu()