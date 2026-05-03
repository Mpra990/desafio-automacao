import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_consultar_inventario():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert "available" in response.json()

def test_consultar_pet_por_status():
    response = requests.get(f"{BASE_URL}/pet/findByStatus?status=available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)