import requests
WEBHOOK_URL = "https://webhook.site/e2223437-27df-4118-8324-0cbaf4358621"  # <-- Replace with your own
data="This is sandbox branch"
# Send POST request
try:
    response = requests.post(WEBHOOK_URL, data=message)
    print(f"POST Status: {response.status_code}")
except Exception as e:
    print(f"Error posting message: {e}")
