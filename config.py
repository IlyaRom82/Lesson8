# === данные ===
API_KEY = "xTNb88MQhhYJDjnMAr4CH-p3Bsey+6+onFcNfBHyCViYAvN0hid7WuFU6tfcyeUu"  # сюда вставьте свой рабочий ключ
COMPANY_ID = "4221f897-b791-4807-a0f2-1fa1e4ddaa23"

# === URL ===
BASE_URL = f"https://ru.yougile.com/api-v2/companies/{COMPANY_ID}"

# === заголовки ===
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
