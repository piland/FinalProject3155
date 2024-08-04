import requests

base_url = "http://127.0.0.1:8000"

def create(promo_id, discount):
    url = f"{base_url}/promoCodes/"
    data = {
        "id": promo_id,
        "discount": discount,
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added promoCode information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add promoCode information: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/promoCodes/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"promoCode information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to get promoCode information: {response.status_code}")
        return None

def read_one(promo_id):
    url = f"{base_url}/paymentInformation/{promo_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"promoCode information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to get promoCode information: {response.status_code}")
        return None

def update(promo_id, discount):
    url = f"{base_url}/paymentInformation/{promo_id}"
    new_data = {}
    if discount is not None:
        new_data["discount"] = discount
    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"promoCode info updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update promoCode info: {response.status_code}")
        return None

def delete(promo_id):
    url = f"{base_url}/promoCodes/{promo_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted promoCode information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete promoCode information: {response.status_code}")
        return None
