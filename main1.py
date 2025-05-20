import os
import requests

# Get token from environment variable
api_dev_key = os.getenv("PASTEBIN_API_KEY")

# Message to post
paste_text = "Hello World from GitHub Actions"

# Pastebin API endpoint
url = "https://pastebin.com/api/api_post.php"

# POST data
payload = {
    'api_dev_key': api_dev_key,
    'api_option': 'paste',
    'api_paste_code': paste_text,
    'api_paste_private': '1',  # 0=public, 1=unlisted, 2=private
    'api_paste_name': 'GitHub Hello World',
    'api_paste_expire_date': '1H'  # Expires in 1 hour
}

response = requests.post(url, data=payload)
print("Response:", response.text)
