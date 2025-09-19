import requests

# === данные ===
api_key = (
    "ВАШ_API_KEY"
)
key_id = (
    "+hur0bipxX2K9h2umRCTb4klwqh-fbl-DuO605Bewj0dvRARQ7fttC8Q25C0glae"
)
# === URL ===
url = "https://ru.yougile.com/api-v2/auth/keys/" + key_id

# === заголовки ===
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# === запрос DELETE ===
response = requests.delete(url, headers=headers)

# === вывод результата ===
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
