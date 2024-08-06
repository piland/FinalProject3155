from api.dependencies.database import SessionLocal

from api.controllers import order_details as order_detail_controller
from api.controllers import payment_information as payment_information_controller
from api.controllers import orders as order_controller
from api.controllers import reviews as review_controller

from api.models.orders import Order
from api.models.order_details import OrderDetail
from api.models.promo_codes import PromoCode
from api.models.sandwiches import Sandwich
from api.models.reviews import Review
from api.models.payment_information import PaymentInformation

from api.db_interface import sandwiches as sandwiches_db
from api.db_interface import recipes as recipes_db
from api.db_interface import resources as resources_db

from api.requests import payment_information as payment_information_request
from api.requests import orders as order_request


#QUESTION: HOW TO PLACE AN ORDER? I DO NOT WISH TO SIGN UP FOR AN ACCOUNT
#TODO: ALERT WHEN ORDER CANNOT BE PROCESSED WHEN TRYING TO ORDER INSTEAD OF THE END
def place_order(account_id):
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
                        "account_id": account_id,
                        "order_type": order_type,
                        "order_status": False
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
                print(f"Your Total is: ${order_total}")
                promo_code_accepted = 0
                while promo_code_accepted == 0:
                    promo_code = input("Enter Promo Code (Leave Blank to Skip): ")
                    if promo_code != "":
                        #try:
                        promo_code_object = db.query(PromoCode).filter(promo_code == PromoCode.name).first()
                        order_total = apply_promo_code(order_total, promo_code_object.name)
                        print(f"Promo Code Accepted! New Total is: ${order_total}")
                        promo_code_accepted = 1
                    #except:
                        print("Promo Code not Accepted")
                    else:
                        promo_code_accepted = 1
                        pass
                try:
                    selected_payment_information = get_payment_information(account_id)
                    if selected_payment_information.balance_on_account > order_total:
                        new_balance = float(selected_payment_information.balance_on_account) - float(order_total)
                        selected_payment_information.balance_on_account = new_balance
                        payment_information_request.update(selected_payment_information.id, balance_on_account=new_balance)
                        print(f"PAYMENT ACCEPTED, NEW BALANCE ON ACCOUNT {selected_payment_information.id}: ${new_balance}")
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
                    resources_db.update_resource(key, amount=value)
            if placing_order == 0:
                break
            created_order = order_controller.create(db, order)
            for order_detail_item in cart:
                order_detail_item.order_id = created_order.id
                order_detail_controller.create(db, order_detail_item)
            placing_order = 0

            leave_review = input("Leave Review of Your Order? (Y/N): ")
            if leave_review.lower() == "y":
                for order_detail_item in cart:
                    write_review(account_id=account_id, sandwich_id=order_detail_item.sandwich_id)

def get_payment_information(account_id):
    with SessionLocal() as db:
        payment_information = db.query(PaymentInformation).filter(account_id == PaymentInformation.id).first()
    return payment_information

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
        if order_item.order_status == False:
            order_status = "IN PROGRESS"
        else:
            order_status = "COMPLETE"
        print(f"\n======= ORDER ID #{order_id} STATUS: {order_status} =======")

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

def write_review(sandwich_id = None, account_id = None):
    with SessionLocal() as db:
        if sandwich_id is not None:
            sandwich = db.query(Sandwich).filter(sandwich_id == Sandwich.id).first()
            stars_accepted = False
            while stars_accepted is False:
                stars = input(f"{sandwich.sandwich_name} Rating (0-5): ")
                try:
                    stars = int(stars)
                    if stars < 0 or stars > 5:
                        print("Star Value Must be Between 0 and 5")
                    else:
                        stars_accepted = True
                except:
                    print("Stars Must be An Integer")
            description = input("Comments (Leave Blank to Skip): ")

            if account_id is None:
                account_id = 1

            review = {
                "stars": stars,
                "description": description,
                "account_id": account_id,
                "sandwich_id": sandwich_id
            }

            review_object = Review(**review)

            review_controller.create(db, review_object)

def get_menu_with_reviews():
    with SessionLocal() as db:
        sandwiches = db.query(Sandwich).all()

        print("======= REVIEWS =======")
        for sandwich_item in sandwiches:
            total_stars = 0
            reviews = db.query(Review).filter(sandwich_item.id == Review.sandwich_id).all()
            for review_item in reviews:
                total_stars += review_item.stars
            avg_sandwich_stars = total_stars/5
            print(f"{sandwich_item.id}. {sandwich_item.sandwich_name}: {avg_sandwich_stars}/5")

def apply_promo_code(order_total, promo_code):
    with SessionLocal() as db:
        promo_code_discount = db.query(PromoCode).filter(promo_code == PromoCode.name).first().discount
        new_total = float(order_total) * float(promo_code_discount)
        return new_total

def show_menu():
    sandwiches_db.show_all_sandwiches()