from api.dependencies.database import SessionLocal
from api.models.sandwiches import Sandwich
from api.models.order_details import OrderDetail
from api.models.orders import Order
from api.models.reviews import Review

from api.requests import orders as orders_request, order_details as order_detail_request

from sqlalchemy import func
from datetime import datetime

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
            print("4. Show Orders Sorted by Popularity")
            print("5. Show Unpopular Orders")
            print("6. Show Low Rated Orders")
            print("7. Show Reviews")
            print("8. Show Only Low-Rated Reviews")
            print("0. Exit to Main Menu")

            try:
                option = int(input("\nEnter One of the Options Above: "))
                if option > -1 and option < 9:
                    valid_option_selected = 1
            except:
                print("Invalid Option")

        if option == 0:
            exit = 1
        elif option == 1:
            show_all_orders()
        elif option == 2:
            show_revenue_on_date()
        elif option == 3:
            show_order_details()
        elif option == 4:
            show_orders_between_dates()
        elif option == 5:
            show_unpopular_orders()
        elif option == 6:
            show_low_rated_orders()
        elif option == 7:
            pass
        valid_option_selected = 0
def show_all_orders():
    with SessionLocal() as db:
        order_list = db.query(Order).all()
        print("===== ALL ORDERS =====")
        for order_item in order_list:
            print(order_item)

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
    with SessionLocal() as db:
        sandwich_list = db.query(Sandwich).all()
        review_list = db.query(Review).all()
        sandwich_reviews_dict = {}
        for sandwich_item in sandwich_list:
            sandwich_reviews_dict[f"{sandwich_item.sandwich_name}"] = 0
            total_reviews = 0
            total_stars = 0
            for review in review_list:
                if review.sandwich_id == sandwich_item.id:
                    total_reviews += 1
                    total_stars += review.stars

            if total_reviews > 0 and total_stars > 0:
                print(sandwich_item.sandwich_name)
                sandwich_reviews_dict[f"{sandwich_item.sandwich_name}"] = total_stars / total_reviews

        sorted_review_dict = dict(sorted(sandwich_reviews_dict.items(), key=lambda item: item[1], reverse=True))

        print("\n===== LIFETIME SANDWICH RATINGS =====")
        for key, value in sorted_review_dict.items():
            print(f"{key}: {value}")

#TODO: SHOW LOW-RATED ORDERS WITH DESCRIPTION
def show_low_rated_orders_details():
    pass

def show_revenue_on_date():
    with SessionLocal() as db:
        date_accepted = 0
        while date_accepted == 0:
            date = input("Enter Date (MM-DD-YYYY): ")
            try:
                date_format = "%m-%d-%Y"
                date_object = datetime.strptime(date, date_format)
                date_accepted = 1
            except:
                print("ERROR: Date Must be In Format (MM-DD-YYYY)")
        orders_on_date = db.query(Order).filter(date_object == func.date(Order.order_date)).all()
        total = 0
        for order_item in orders_on_date:
            for order_detail_item in order_item.order_details:
                sandwich = db.query(Sandwich).filter(order_detail_item.sandwich_id == Sandwich.id).first()
                total += sandwich.price * order_detail_item.amount
        print(f"\n===============\nTOTAL REVENUE FOR {date_object}: ${total}\n===============")

def show_orders_between_dates():
    with SessionLocal() as db:
        date_accepted = 0
        date_format = "%m-%d-%Y"
        while date_accepted == 0:
            date = input("Enter First Date (MM-DD-YYYY): ")
            try:
                date_object = datetime.strptime(date, date_format)
                date_accepted = 1
            except:
                print("ERROR: Date Must be In Format (MM-DD-YYYY)")
        date_two_accepted = 0
        while date_two_accepted == 0:
            date = input("Enter Second Date (MM-DD-YYYY): ")
            try:
                date_two_object = datetime.strptime(date, date_format)
                date_two_accepted = 1
            except:
                print("ERROR: Date Must be In Format (MM-DD-YYYY)")
        orders_between_dates = db.query(Order).filter((date_object <= func.date(Order.order_date)) & (date_two_object >= func.date(Order.order_date))).all()
        for order_item in orders_between_dates:
            print(order_item)