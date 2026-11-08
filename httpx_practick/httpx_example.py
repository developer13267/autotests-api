import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response =httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)  # 200
print(response.json())
print(response.request.headers)

data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())
print(response.request.headers)


headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.json())
print(response.request.headers)


params = [("userId", 1), ("userId", 2)]
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#или response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач


files = {"file": ("example.txt", open("../example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())  # Ответ с данными о загруженном файле

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.json())
print(response2.json())


client = httpx.Client(headers = {"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/ijk")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса {e}")



try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
