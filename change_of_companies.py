import requests
from config import BASE_URL, HEADERS


def test_update_project():
    # --- данные для обновления ---
    new_title = "Project One 03-25"
    payload = {
        "deleted": True,
        "title": new_title,
        "apiData": "{}"
    }

    # --- запрос PUT ---
    put_response = requests.put(BASE_URL, json=payload, headers=HEADERS)
    assert put_response.status_code == 200  # проверяем успешный запрос

    # --- запрос GET для проверки изменений ---
    get_response = requests.get(BASE_URL, headers=HEADERS)
    assert get_response.status_code == 200  # проверяем успешный запрос

    project_data = get_response.json()

    # --- проверки результата ---
    assert "title" in project_data, "В ответе нет поля 'title'"
    assert project_data["title"] == new_title
