import requests
from config import API_KEY

def test_get_companies():
    url = "https://ru.yougile.com/api-v2/companies"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Запрос не удался: {response.text}"

    data = response.json()
    # проверяем, что это словарь
    assert isinstance(data, dict), "Ожидался словарь с деталями компании"

    # проверяем наличие ключевых полей
    assert "id" in data, "Нет поля 'id'"
    assert "title" in data, "Нет поля 'title'"
