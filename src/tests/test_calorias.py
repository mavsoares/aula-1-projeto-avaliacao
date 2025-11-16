from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200


def test_calorias():
    payload = {
        "alimentos": [
            {"nome": "arroz", "gramas": 150},
            {"nome": "feijao", "gramas": 100},
            {"nome": "frango", "gramas": 100},
        ]
    }
    response = client.post("/calcular", json=payload)
    assert response.status_code == 200
    assert response.json()["total_calorias"] == 450


def test_alimento_nao_encontrado():
    payload = {
        "alimentos": [
            {"nome": "batata", "gramas": 250},
            {"nome": "feijao", "gramas": 100},
            {"nome": "frango", "gramas": 100},
        ]
    }
    response = client.post("/calcular", json=payload)
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Alimento 'batata' não encontrado na tabela de calorias"
    )
