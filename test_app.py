import pytest
from app import app  # Импортируем Flask-приложение из app.py

# Фикстура для создания тестового клиента
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Тест 1: Проверяем главную страницу
def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200  # Проверяем код ответа
    assert b"Hello, CI/CD World!" in response.data  # Проверяем текст

# Тест 2: Проверяем несуществующий путь
def test_404_route(client):
    response = client.get('/non-existent-page')
    assert response.status_code == 404
