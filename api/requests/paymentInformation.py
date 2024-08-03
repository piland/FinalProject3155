import requests

base_url = "http://127.0.0.1:8000"

def create(card_information, balance_on_account, payment_type, last_transaction_status):
    url = f"{base_url}/paymentInformation/"
    data = {
        "cardInformation": card_information,
        "balanceOnAccount": balance_on_account,
        "paymentType": payment_type,
        "lastTransactionStatus": last_transaction_status
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added Payment Information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add Payment Information: {response.status_code}")
        return None


def read_all():
    url = f"{base_url}/paymentInformation/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Customer Payment Information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Payment Information: {response.status_code}")
        return None

def read_one(payment_information_id):
    url = f"{base_url}/paymentInformation/{payment_information_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Customer Payment Information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Payment Information: {response.status_code}")
        return None

def update(payment_information_id, card_information = None, balance_on_account = None, payment_type = None, last_transaction_status = None):
    url = f"{base_url}/paymentInformation/{payment_information_id}"
    new_data = {}
    if card_information is not None:
        new_data["cardInformation"] = card_information
    if balance_on_account is not None:
        new_data["balanceOnAccount"] = balance_on_account
    if payment_type is not None:
        new_data["paymentType"] = payment_type
    if last_transaction_status is not None:
        new_data["lastTransactionStatus"] = last_transaction_status
    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"Payment Info Updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Update Payment Info: {response.status_code}")
        return None

def delete(payment_information_id):
    url = f"{base_url}/paymentInformation/{payment_information_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted Payment Information: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete Payment Information: {response.status_code}")
        return None
