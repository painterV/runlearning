import requests

# 发送简单的POST请求
data = {"username": "user1", "password": "pass123"}
response = requests.post("https://example.com/login", data=data)
print("Status Code:", response.status_code)
print("Response Content:", response.text)

# 发送JSON数据的POST请求
json_data = {"name": "John", "age": 30}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=json_data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# 上传文件的POST请求
files = {'file': open('example.txt', 'rb')}
response = requests.post("https://example.com/upload", files=files)
print("Status Code:", response.status_code)