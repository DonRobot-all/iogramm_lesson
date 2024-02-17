# import requests

# def get_users():
#     url = 'https://jsonplaceholder.typicode.com/users'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         users = response.json()
#         return users
#     else:
#         print(f'Ошибка при выполнении запроса: {response.status_code}')
#         return None

# def main():
#     users = get_users()
#     if users:
#         for user in users:
#             print(f"Имя: {user['name']}, Почта: {user['email']}")

# if __name__ == '__main__':
#     main()
import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Не удалось получить данные. Код ошибки: {response.status_code}")
