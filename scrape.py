import requests

# URL for "car cover" search on OLX
url = "https://www.olx.in/items/q-car-cover"

# Headers to simulate real browsers
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open("olx_car_cover.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Search results saved to olx_car_cover.html")
else:
    print(f"Failed to retrieve page")
