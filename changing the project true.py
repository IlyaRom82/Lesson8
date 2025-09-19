import requests

# === данные ===
api_key = (
    "xTNb88MQhhYJDjnMAr4CH-p3Bsey+6+onFcNfBHyCViYAvN0hid7WuFU6tfcyeUu"
)
project_id = (
    "3acc4493-031b-4488-8e35-8ebbd3695e9a"
)
# === URL ===
url = f"https://ru.yougile.com/api-v2/projects/{project_id}"

# === тело запроса ===
payload = {
    "deleted": True,
    "title": "Пример проекта",
    "users": {
        "3de9fd20-c7e1-4eaa-a87f-52aa2ca1707e": "admin",
    }
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
