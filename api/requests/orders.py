from api.models.orders import Order
from api.models.order_details import OrderDetail
from api.models.sandwiches import Sandwich
from api.models.recipes import Recipe
from api.models.promo_codes import PromoCode
import requests
import json

base_url = "http://127.0.0.1:8000"

def create(customer_name, description):
    url = f"{base_url}/orders/"
    data = {
        "customer_name": customer_name,
        "description": description
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added Order: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add Order: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/orders/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Orders: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Orders: {response.status_code}")
        return None

def show_all_orders():
    order_dicts = read_all()
    print("===== ORDERS =====")
    for order_dict in order_dicts:
        print(f"ID: {order_dict["id"]}, NAME: {order_dict["customer_name"]}, DATE: {order_dict["order_date"]}, DESC: {order_dict["description"]}, TYPE: {order_dict["order_type"]}, ACCOUNT: {order_dict["account_id"]}")

def read_one(item_id):
    url = f"{base_url}/orders/{item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Orders: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Orders: {response.status_code}")
        return None

def update(item_id, customer_name = None, description = None):
    url = f"{base_url}/orders/{item_id}"
    new_data = {}
    if customer_name is not None:
        new_data["customer_name"] = customer_name
    if description is not None:
        new_data["description"] = description
    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"Order Info Updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update Info: {response.status_code}")
        return None

def delete(item_id):
    url = f"{base_url}/orders/{item_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted Order: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete Order: {response.status_code}")
        return None