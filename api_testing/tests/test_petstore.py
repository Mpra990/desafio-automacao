import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# --- TESTES DO MÓDULO: PET ---
def test_post_pet():
    """Cria um novo pet na loja"""
    payload = {
        "id": 990,
        "name": "Rex",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_get_pet_by_status():
    """Busca pets por status (disponibilidade)"""
    response = requests.get(f"{BASE_URL}/pet/findByStatus?status=available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# --- TESTES DO MÓDULO: STORE ---
def test_get_inventory():
    """Valida o inventário da loja"""
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert "available" in response.json()

def test_post_order():
    """Simula a compra de um pet"""
    payload = {
        "id": 1,
        "petId": 990,
        "quantity": 1,
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

# --- TESTES DO MÓDULO: USER ---
def test_create_user():
    """Cria um novo usuário no sistema"""
    payload = {
        "id": 1,
        "username": "mpra_dev",
        "firstName": "M",
        "lastName": "Pra",
        "email": "teste@teste.com",
        "password": "123",
        "phone": "99999999",
        "userStatus": 1
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200

def test_login_user():
    """Realiza o login do usuário criado"""
    response = requests.get(f"{BASE_URL}/user/login?username=mpra_dev&password=123")
    assert response.status_code == 200
    assert "logged in user session" in response.json()["message"]