import requests

url = "https://ru.yougile.com/api-v2/auth/keys/get"

payload = {
    "login": "ria478217@gmail.com",       # ваш email
    "password": "ArTupaLois182!",         # ваш пароль
    "companyId": "4221f897-b791-4807-a0f2-1fa1e4ddaa23"  # ваш companyId
}

headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
