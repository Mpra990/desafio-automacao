import requests

BASE_URL = "https://petstore.swagger.io/v2"

# --- PET ---
def test_api_post_pet():
    payload = {"id": 990, "name": "Rex", "status": "available"}
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200

def test_api_get_pet_404():
    response = requests.get(f"{BASE_URL}/pet/99999988")
    assert response.status_code == 404

# --- STORE ---
def test_api_store_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200

def test_api_post_order():
    payload = {"id": 1, "petId": 990, "quantity": 1, "status": "placed"}
    response = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200

# --- USER ---
def test_api_create_user():
    payload = {"id": 1, "username": "mpra_dev", "password": "123"}
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200

def test_api_user_login():
    params = {"username": "mpra_dev", "password": "123"}
    response = requests.get(f"{BASE_URL}/user/login", params=params)
    assert response.status_code == 200