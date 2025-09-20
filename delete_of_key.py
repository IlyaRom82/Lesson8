import requests
from config import API_KEY  # берём ключ из config.py

def test_delete_api_key():
    key_id = "+hur0bipxX2K9h2umRCTb4klwqh-fbl-DuO605Bewj0dvRARQ7fttC8Q25C0glae"

    url = f"https://ru.yougile.com/api-v2/auth/keys/{key_id}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.delete(url, headers=headers)

    assert response.status_code == 200
