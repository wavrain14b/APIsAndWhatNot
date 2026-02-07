import requests

url = "https://jsonplaceholder.com/posts/1"

response = requests.get(url)

print("Status: code: ", response.status_code)
print("Content-Type: ", response.headers.get("Content-Type"))

data = response.json()
print("Post title: ", data["title"])

print(data)