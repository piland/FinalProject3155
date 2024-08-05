from api.dependencies.database import SessionLocal
from api.models.sandwiches import Sandwich
from api.models.order_details import OrderDetail
from api.models.orders import Order

def report_menu():
    exit = 0
    valid_option_selected = 0
    while exit != 1:
        while valid_option_selected != 1:
            option = -1
            print("\n======= REPORTS ========")
            print("1. Show Current Orders")
            print("2. Get Revenue Report")
            print("3. Show Order Details")
            print("4. Show Unpopular Orders")
            print("5. Show Low Rated Orders")
            print("6. Show Reviews")
            print("7. Show Only Low-Rated Reviews")
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
        elif option == 2:
            pass
        elif option == 3:
            show_order_details()
        elif option == 4:
            show_unpopular_orders()
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        valid_option_selected = 0

#QUESTION: HOW DOES THE SYSTEM ALERT ME IF THERE ARE INSUFFICIENT INGREDIENTS TO FULFILL AN ORDER?
#TODO: SHOW WHEN THERE ARENT ENOUGH INGREDIENTS
def is_enough_ingredients():
    pass

#QUESTION: HOW CAN I VIEW THE LIST OF ALL ORDERS? IS THERE AN OPTION TO VIEW THE DETAILS OF A SPECIFIC ORDER?
#TODO: VIEW ALL ORDERS
def show_all_orders():
    with SessionLocal() as db:
        order_list = db.query(Order).all()
        print("===== ALL ORDERS =====")
        for order_item in order_list:
            print(order_item)

#TODO: VIEW ORDER DETAILS
def show_order_details():
    with SessionLocal() as db:
        show_all_orders()
        order_id_accepted = 0
        while order_id_accepted == 0:
            order_id = input("Enter ID of Order to Get Details: ")
            try:
                order_id = int(order_id)
                order_detail_list = db.query(OrderDetail).filter(OrderDetail.order_id == order_id).all()
                order_id_accepted = 1
            except:
                print("Order ID must be Integer and Exist in Orders")
        print(f"===== ORDER ID {order_id} DETAILS =====")
        for order_detail_item in order_detail_list:
            sandwich_name = db.query(Sandwich).filter(order_detail_item.sandwich_id == Sandwich.id).first().sandwich_name
            print(f"ID: {order_detail_item.id}, ORDER_ID: {order_id}, SANDWICH: {sandwich_name}, AMOUNT: {order_detail_item.amount}")

#QUESTION: HOW CAN I IDENTIFY DISHES THAT ARE LESS POPULAR OR HAVE RECEIVED COMPLAINTS? IS THERE A WAY TO UNDERSTAND CUSTOMER DISATISFACTION?
#TODO: VIEW UNPOPULAR ORDERS (Im just gonna show all sandwiches in descending order based on sales)
def show_unpopular_orders():
    with SessionLocal() as db:
        sandwich_list = db.query(Sandwich).all()
        order_detail_list = db.query(OrderDetail).all()
        sandwich_sales_dict = {}
        for sandwich_item in sandwich_list:
            sandwich_sales_dict[f"{sandwich_item.sandwich_name}"] = 0
            for order_detail_item in order_detail_list:
                if order_detail_item.sandwich_id == sandwich_item.id:
                    sandwich_sales_dict[f"{sandwich_item.sandwich_name}"] += order_detail_item.amount
        sorted_order_detail_dict = dict(sorted(sandwich_sales_dict.items(), key=lambda item: item[1], reverse=True))

        print("\n===== LIFETIME SANDWICH ORDERS =====")
        for key, value in sorted_order_detail_dict.items():
            print(f"{key}: {value}")

#TODO: SHOW LOW-RATED ORDERS, ASK FOR THRESHOLD (eg. less than 2 stars)
def show_low_rated_orders():
    pass

#TODO: SHOW LOW-RATED ORDERS WITH DESCRIPTION
def show_low_rated_orders_details():
    pass

#QUESTION: HOW CAN I DETERMINE THE TOTAL REVENUE GENERATED FROM FOOD SALES ON ANY GIVEN DAY?
#TODO: SHOW TOTAL REVENUE
def show_revenue_on_date():
    pass
    #TODO: sum orders totals on date

#QUESTION: IS THERE A WAY TO VIEW THE LIST OF ORDERS WITHIN A SPECIFIC DATE RANGE?
#TODO: LIST OF ORDER IN DATE RANGE
def show_orders_between_dates():
    pass
    #TODO: filter order_list to show only between start_date and end_date