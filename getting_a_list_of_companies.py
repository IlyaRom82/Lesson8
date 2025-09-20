import requests
from config import API_KEY

def test_get_companies_list():
    url = "https://ru.yougile.com/api-v2/companies"  # URL для получения компаний

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Запрос не удался: {response.text}"

    data = response.json()

    # Проверяем, что вернулся словарь с нужными полями
    assert isinstance(data, dict), "Ожидался словарь с данными компании"

    required_fields = ["id", "title", "timestamp", "deleted", "apiData"]
    for field in required_fields:
        assert field in data, f"В ответе нет поля '{field}'"

    # Дополнительно можно проверить, что название компании непустое
    assert data["title"], "Название компании пустое"
