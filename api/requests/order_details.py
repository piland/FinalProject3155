import requests

base_url = "http://127.0.0.1:8000"

def create(amount, order_id, sandwich_id):
    url = f"{base_url}/orderdetails/"
    data = {
        "amount": amount,
        "order_id": order_id,
        "sandwich": sandwich_id
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added Order Details: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add Order Details: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/orderdetails/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Customer Order Details: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Order Details: {response.status_code}")
        return None

def read_one(item_id):
    url = f"{base_url}/orderdetails/{item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Customer Order Details: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Order Details: {response.status_code}")
        return None

def update(item_id, amount = None, order_id = None, sandwich_id = None):
    url = f"{base_url}/orderdetails/{item_id}"
    new_data = {}
    if amount is not None:
        new_data["amount"] = amount
    if order_id is not None:
        new_data["order_id"] = order_id
    if sandwich_id is not None:
        new_data["sandwich_id"] = sandwich_id
    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"Payment Info Updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update Payment Info: {response.status_code}")
        return None

def delete(item_id):
    url = f"{base_url}/orderdetails/{item_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted Order Details: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete Order Details: {response.status_code}")
        return None