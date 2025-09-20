import requests
from config import API_KEY

def test_get_projects():
    url = "https://ru.yougile.com/api-v2/projects"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Запрос не удался: {response.text}"

    data = response.json()

    # Проверяем, что это словарь с ключами 'content' и 'paging'
    assert isinstance(data, dict), "Ожидался словарь"
    assert "content" in data, "Нет поля 'content'"
    assert "paging" in data, "Нет поля 'paging'"
    assert isinstance(data["content"], list), "'content' должен быть списком"

    # Если список не пустой, проверяем поля первого проекта
    if data["content"]:
        first_project = data["content"][0]
        required_fields = ["id", "title", "deleted", "timestamp", "apiData"]
        for field in required_fields:
            assert field in first_project, f"В первом проекте нет поля '{field}'"
