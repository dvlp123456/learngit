import requests
# Author: Warren Yu

# curl -v  -H 'Content-Type: application/json' http://localhost:4077/hotels?lang=zh_CN
url = "http://localhost:4077/hotels?lang=zh_CN"
data = requests.get(url)

# Comment: This is other comment content

print data.json
