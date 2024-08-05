from api.dependencies.database import SessionLocal

from api.controllers import order_details as order_detail_controller
from api.controllers import payment_information as payment_information_controller
from api.controllers import orders as order_controller

from api.models.orders import Order
from api.models.order_details import OrderDetail
from api.models.promo_codes import PromoCode
from api.models.sandwiches import Sandwich

from api.db_interface import sandwiches as sandwiches_db
from api.db_interface import recipes as recipes_db
from api.db_interface import resources as resources_db

from api.requests import payment_information as payment_information_request
from api.requests import orders as order_request


#QUESTION: HOW TO PLACE AN ORDER? I DO NOT WISH TO SIGN UP FOR AN ACCOUNT
#TODO: ALERT WHEN ORDER CANNOT BE PROCESSED WHEN TRYING TO ORDER INSTEAD OF THE END
def place_order():
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
                    order_type = get_order_type(order_type)

                    order_data = {
                        "customer_name": customer_name,
                        "description": description,
                        "account_id": 1,
                        "order_type": order_type
                    }
                    order = Order(**order_data)
                    order_created = 1

                sandwiches_db.show_all_sandwiches()
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
                sandwich = sandwiches_db.get_sandwich_by_id(sandwich_id)
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
                price = sandwiches_db.get_sandwich_by_id(sandwich_id).price
                order_total += (price * order_detail.amount)

            payment_information_accepted = 0
            while payment_information_accepted == 0:
                show_all_payment_information()
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
                        payment_information_request.update(payment_id, balance_on_account=new_balance)
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
            resources_db.show_all_resources()
            if placing_order == 0:
                break
            created_order = order_controller.create(db, order)
            for order_detail_item in cart:
                order_detail_item.order_id = created_order.id
                order_detail_controller.create(db, order_detail_item)
            placing_order = 0
            print("Finish!")

def show_all_payment_information():
    with SessionLocal() as db:
        payment_information_list = payment_information_controller.read_all(db)
        print("===== PAYMENT INFORMATION =====")
        for payment_info in payment_information_list:
            print(payment_info)

def get_order_type(type):
    type = "Dine-In"
    if input == 2:
        type = "Takeout"
    elif input == 3:
        type = "Delivery"
    return type

def check_order():
    #ORDER TABLE FOR DEMONSTRATION PURPOSES ONLY, CUSTOMER SHOULD KNOW ORDER NUMBER THEORETICALLY
    with SessionLocal() as db:
        order_request.show_all_orders()
        order_id_accepted = 0
        while order_id_accepted == 0:
            order_id = input("Input Order ID to Check Status: ")
            try:
                order_id = int(order_id)
                order_item = db.query(Order).filter(Order.id == order_id).first()
                order_id_accepted = 1
            except:
                print("ERROR: Order ID must be Integer and Exist in Order Table")
        print(f"ORDER ID: {order_id} STATUS: #NEED ORDER STATUS")

#QUESTION: IS THERE A FEATURE THAT ALLOWS ME TO SEARCH FOR SPECIFIC TYPES OF FOOD?
#TODO: IMPLEMENT SORTING FUNCTION FOR MENU ITEMS
def get_filtered_menu():
    with SessionLocal() as db:
        sandwich_list = db.query(Sandwich).all()
        tags = []
        for sandwich_item in sandwich_list:
            exists = 0
            for existing_tag in tags:
                if sandwich_item.tags == existing_tag:
                    exists = 1
            if exists == 0:
                if sandwich_item.tags != "":
                    tags.append(sandwich_item.tags)
        print("\n======= AVAILABLE FILTERS ========")
        print(f"{tags}")
        filter_accepted = 0
        while filter_accepted == 0:
            requested_filter = input("\nEnter Requested Filter (Exit/e to Exit): ")
            if requested_filter.lower() == "exit" or requested_filter.lower() == "e":
                break
            else:
                for tag in tags:
                    if requested_filter.lower() == tag.lower():
                        filter_accepted = 1
                if filter_accepted == 0:
                    print("Filter not Found!")
        if filter_accepted == 1:
            filtered_menu_options = db.query(Sandwich).filter(requested_filter == Sandwich.tags)
            print("======= FILTERED MENU =======")
            for menu_option in filtered_menu_options:
                print(f"{menu_option.id}. {menu_option.sandwich_name}")

#QUESTION: HOW CAN I RATE AND REVIEW DISHES I'VE ORDERED?
#TODO: IMPLEMENT BOTH GET AND PUT REVIEW FUNCTIONS
#TODO: DONT WE NEED TO SPECIFY WHAT ITEM WERE REVIEWING?
def write_review():
    pass

def get_reviews_for_single_item():
    pass

def get_menu_with_reviews():
    pass

#QUESTION: HOW DO I APPLY A PROMOTIONAL CODE TO ME ORDER?
#TODO: APPLY PROMOTIONAL CODE TO ORDER
def apply_promo_code(order_total, promo_code):
    with SessionLocal() as db:
        promo_code_discount = db.query(PromoCode).filter(promo_code == PromoCode.name).first().discount
        new_total = order_total * promo_code_discount
        return new_total

def show_menu():
    sandwiches_db.show_all_sandwiches()

get_filtered_menu()