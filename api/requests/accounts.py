import requests

base_url = "http://127.0.0.1:8000"


def create(name, age, phone_number, email, role_id, password, payment_information_id):
    url = f"{base_url}/accounts/"
    data = {
        "name": name,
        "age": age,
        "phone_number": phone_number,
        "email": email,
        "role_id": role_id,
        "password": password,
        "payment_information_id": payment_information_id
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Added Account: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add Account: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/accounts/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"All Customer Accounts: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get All Accounts: {response.status_code}")
        return None


def read_one(account_id):
    url = f"{base_url}/accounts/{account_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Customer Account: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Account: {response.status_code}")
        return None


def update(account_id, name=None, age=None, phone_number=None, email=None, role_id=None, password=None,
           payment_information_id=None):
    url = f"{base_url}/accounts/{account_id}"
    new_data = {}
    if name is not None:
        new_data["name"] = name
    if age is not None:
        new_data["age"] = age
    if phone_number is not None:
        new_data["phone_number"] = phone_number
    if email is not None:
        new_data["email"] = email
    if role_id is not None:
        new_data["role_id"] = role_id
    if password is not None:
        new_data["password"] = password
    if payment_information_id is not None:
        new_data["payment_information_id"] = payment_information_id
    response = requests.put(url, json=new_data)
    if response == 200:
        print(f"Payment Info Updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update Payment Info: {response.status_code}")
        return None


def delete(account_id):
    url = f"{base_url}/accounts/{account_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted Account: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete Account: {response.status_code}")
        return None
