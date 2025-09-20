import requests
from config import API_KEY

def test_update_project():
    project_id = "3acc4493-031b-4488-8e35-8ebbd3695e9a"
    url = f"https://ru.yougile.com/api-v2/projects/{project_id}"

    payload = {
        "deleted": True,
        "title": "Пример проекта",
        "users": {
            "3de9fd20-c7e1-4eaa-a87f-52aa2ca1707e": "admin"
        }
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # === запрос PUT ===
    response = requests.put(url, json=payload, headers=headers)

    # === проверки ===
    assert response.status_code == 200, f"Запрос не удался: {response.text}"

    data = response.json()

    # Проверяем, что вернулся словарь с полем 'id'
    assert isinstance(data, dict), "Ожидался словарь в ответе"
    assert "id" in data, "В ответе нет поля 'id'"
    assert data["id"] == project_id, "ID проекта не совпадает с отправленным"
