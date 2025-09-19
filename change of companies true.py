import requests

# === данные ===
api_key = (
    "xTNb88MQhhYJDjnMAr4CH-p3Bsey+6+onFcNfBHyCViYAvN0hid7WuFU6tfcyeUu"
)

# сюда вставьте свой рабочий ключ


company_id = (
    "4221f897-b791-4807-a0f2-1fa1e4ddaa23"
)
# === URL ===
url = (
    f"https://ru.yougile.com/api-v2/companies/{company_id}"
)  # звездочка * в curl заменяется на конкретный ID

# === тело запроса ===
payload = {
    "deleted": True,
    "title": "Project One 03-25",
    "apiData": "{}"
}

# === заголовки ===
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# === запрос PUT ===
response = requests.put(url, json=payload, headers=headers)

# === вывод результата ===
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
