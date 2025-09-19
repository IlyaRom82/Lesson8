import requests

url = "https://ru.yougile.com/api-v2/auth/companies"

payload = {
    "login": "ria478217@gmail.com",
    "password": "ArTupaLois182!",
    "name": "SkyLite"   # название вашей компании
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
