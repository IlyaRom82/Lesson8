import requests

# === данные ===
api_key = (
    "xTNb88MQhhYJDjnMAr4CH-p3Bsey+6+onFcNfBHyCViYAvN0hid7WuFU6tfcyeUu"
)
# === URL ===
url = (
    "https://ru.yougile.com/api-v2/companies"
)
# === заголовки ===
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# === запрос GET ===
response = requests.get(url, headers=headers)

# === вывод результата ===
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.json())  # если сервер вернул JSON
