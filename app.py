import requests

response = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=2370068")

print(response)
print(response.text)
