import requests

base_url = "http://127.0.0.1:8000"

def create(stars, description):
    url = f"{base_url}/reviews/"
    data = {
        "stars": stars,
        "description": description,
        "account_id": account_id,
        "sandwich_id": sandwich_id
    }
    response = requests.post(url, json = data)
    if response.status_code == 200:
        print(f"Added Review: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Add Reviews: {response.status_code}")
        return None

def read_all():
    url = f"{base_url}/reviews/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Reviews: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Reviews: {response.status_code}")
        return None

def read_one(review_id):
    url = f"{base_url}/reviews/{review_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Reviews: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Get Reviews: {response.status_code}")
        return None

def update(review_id, stars = None, description = None):
    url = f"{base_url}/reviews/{review_id}"
    new_data = {}
    if stars is not None:
        new_data["stars"] = stars
    if description is not None:
        new_data["description"] = description
    response = requests.put(url, json = new_data)
    if response == 200:
        print(f"Review Updated: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Review Info: {response.status_code}")
        return None

def delete(review_id):
    url = f"{base_url}/reviews/{review_id}"
    response = requests.delete(url)
    if response == 200:
        print(f"Deleted Reviews: {response.json()}")
        return response.json()
    else:
        print(f"Failed to Delete Reviews: {response.status_code}")
        return None