import requests
import json

# Your Marketstack API access key
API_KEY = ""


# Marketstack API endpoint for historical data
url = "https://api.marketstack.com/v1/eod"

#parameters
params = {
    "access_key": API_KEY,
    "symbols": "NVDA",
    "date_from": "2025-09-29",
    "date_to": "2025-10-03",
    "limit": 1000,  # optional: max results per page
}

# Make the request
response = requests.get(url, params=params)
data = response.json()

print(data)
