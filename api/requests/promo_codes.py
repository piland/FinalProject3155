import requests

base_url = "http://127.0.0.1:8000"

def create(discount, name):
    url = f"{base_url}/promocodes/"
    data = {
        "discount": discount,
        "name": name,
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added promo_code information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add promo_code information: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/promocodes/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"promo_code information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to get promo_code information: {response.status_code}")
        return None

def read_one(name):
    url = f"{base_url}/promocodes/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"promo_code information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to get promo_code information: {response.status_code}")
        return None

def update(name, discount):
    url = f"{base_url}/promocodes/{name}"
    new_data = {}
    if discount is not None:
        new_data["discount"] = discount

    if name is not None:
        new_data["name"] = name

    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"promo_code info updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update promo_code info: {response.status_code}")
        return None

def delete(name):
    url = f"{base_url}/promocodes/{name}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted promo_code information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete promo_code information: {response.status_code}")
        return None
