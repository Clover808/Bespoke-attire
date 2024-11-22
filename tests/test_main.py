from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    
def test_search_products():
    response = client.get("/search?q=fabric")
    assert response.status_code == 200

def test_category_filter():
    response = client.get("/products?category=fabrics")
    assert response.status_code == 200
    data = response.json()
    assert all(product["category"] == "fabrics" for product in data["products"])
