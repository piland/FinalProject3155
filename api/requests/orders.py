import requests

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