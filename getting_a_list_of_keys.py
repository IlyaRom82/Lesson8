import requests


def test_get_api_keys():
    url = "https://ru.yougile.com/api-v2/auth/keys/get"

    payload = {
        "login": "ria478217@gmail.com",       # ваш email
        "password": "ArTupaLois182!",         # ваш пароль
        "companyId": "4221f897-b791-4807-a0f2-1fa1e4ddaa23"  # ваш companyId
    }

    headers = {
        "Content-Type": "application/json",
    }

    # --- запрос ---
    response = requests.post(url, json=payload, headers=headers)

    # --- проверки ---
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list), "Ожидался список ключей"
    assert len(data) > 0, "Список ключей пуст"

    # проверяем структуру первого элемента
    first_key = data[0]
    assert "key" in first_key, "Нет ключа 'key' в ответе"
    assert "companyId" in first_key, "Нет ключа 'companyId' в ответе"
    assert "timestamp" in first_key, "Нет ключа 'timestamp' в ответе"
    assert len(first_key["key"]) > 0, "API-ключ пустой"
