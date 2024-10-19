import requests

# тестирование списка товаров
# url = "http://localhost:8000/api/products/"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEwODI1LCJpYXQiOjE3MjkyMTA1MjUsImp0aSI6ImRkMzRkN2FmODc4MzRiMTJhMWQ5OGI1NTcwN2E0YTBjIiwidXNlcl9pZCI6Mn0.GifhYY34REI43HoYv0vDIevWeTmw7uWYX1l_VYXClUg"  # ваш токен доступа
# }
#
# response = requests.get(url, headers=headers)
# print(response.json())



# Получение спецификации по отдельному товару в базе данных
# здесь тестирую получение спецификации по id товара
# url = "http://localhost:8000/api/products/1/"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEwODI1LCJpYXQiOjE3MjkyMTA1MjUsImp0aSI6ImRkMzRkN2FmODc4MzRiMTJhMWQ5OGI1NTcwN2E0YTBjIiwidXNlcl9pZCI6Mn0.GifhYY34REI43HoYv0vDIevWeTmw7uWYX1l_VYXClUg"  # ваш токен доступа
# }
#
# response = requests.get(url, headers=headers)
# print(response.json())



# здесь тестирую добавление/удаление товара из корзины
# url = 'http://localhost:8000/api/cart/add/'
#
# data = {
#     "order": 1,
#     "product": 1,
#     "shop": 1,
#     "quantity": 2
# }
#
# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjExNTAxLCJpYXQiOjE3MjkyMTEyMDEsImp0aSI6ImE0NWNjNjQyN2Q5YzQzN2M5MWU5ODQyNjJjNGMwZjJhIiwidXNlcl9pZCI6Mn0.UEcu6_aUNDXbzKZLIuLd5-JzLEVaBcmW741WgIsDk9Y',  # Замените на ваш токен
#     'Content-Type': 'application/json'
# }
#
# # Отправка POST-запроса
# response = requests.post(url, json=data, headers=headers)
#
# # Вывод ответа
# print(response.status_code)
# print(response.json())



# здесь тестирую добавление/удаление адреса доставки
# ДОБАВЛЕНИЕ
# url = 'http://localhost:8000/api/delivery-address/'
#
# data = {
#     "user": 2,  # (1 - admin, 2 - username)
#     "address_line": "123 Main St",
#     "city": "Moscow",
#     "postal_code": "101000",
#     "country": "Russia"
# }

# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEyNDUzLCJpYXQiOjE3MjkyMTIxNTMsImp0aSI6ImVjMDY5MjVhZWU1YzQ0YjE4NGU3M2Y0Y2MwNWVhM2I2IiwidXNlcl9pZCI6Mn0.F32nBixjs7aWDtKmziBk2tSEfrhZ3Qio1ILGDULRG5k',
#     'Content-Type': 'application/json'
# }
#
# # Отправка POST-запроса
# response = requests.post(url, json=data, headers=headers)
#
# print(response.status_code)
# print(response.json())

# УДАЛЕНИЕ
# address_id = 6  # Замените на реальный ID адреса
# url = f'http://localhost:8000/api/delivery-address/{address_id}/'
#
# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEyNzI4LCJpYXQiOjE3MjkyMTI0MjgsImp0aSI6ImM4ZmNmMGU2Y2MwNDQyZjk4ZDY3ZTc2ZTA4YTM4MzkzIiwidXNlcl9pZCI6Mn0.lkSacC0sa3pzhz-1ITYnNWKjhkYyZAlvkdxhXQKBaog',
#     'Content-Type': 'application/json'
# }
#
# response = requests.delete(url, headers=headers)
#
# if response.status_code == 204:
#     print(f"Код ответа: {response.status_code}")
#     print("Адрес доставки успешно удален.")
# else:
#     try:
#         print(response.json())  # Обрабатываем JSON-ответ, если он есть
#     except requests.exceptions.JSONDecodeError:
#         print("Ответ сервера не содержит JSON.")
#         print(f"Код ответа: {response.status_code}, Текст ответа: {response.text}")



# здесь тестирую получение списка заказов
# url = 'http://localhost:8000/api/orders/'
# headers = {
#     'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEzMjczLCJpYXQiOjE3MjkyMTI5NzMsImp0aSI6IjliY2U0NGQyNjgzNDRhMjY4NDg4Njg5NzY0NTlhNDA0IiwidXNlcl9pZCI6Mn0.QKckaKzUa3CFWfqK8p9yeZI_mPol0KSm21pbIkRB4Hc',  # Используйте ваш токен
# }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     orders = response.json()
#     print("Список заказов:", orders)
# else:
#     print(f"Ошибка: {response.status_code} - {response.text}")

# здесь тестирую получение деталей заказа по его id
# order_id = 2  # Замените на ID вашего заказа
# url = f'http://localhost:8000/api/orders/{order_id}/'
# headers = {
#     'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjEzNjg1LCJpYXQiOjE3MjkyMTMzODUsImp0aSI6IjU3MDQ4NDQ2NWRjYTQ3Y2E4ZDMxMTY1MDg0MzllN2RjIiwidXNlcl9pZCI6Mn0.kr0WnDxNKGnP3n7A1vQqrwyudb7SCxsUrRbKiueQDts',  # Используйте ваш токен
# }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     order_details = response.json()
#     print("Детали заказа:", order_details)
# else:
#     print(f"Ошибка: {response.status_code} - {response.text}")



# здесь тестирую изменение статуса заказа
# order_id = 1  # Замените на ID вашего заказа
# url = f'http://localhost:8000/api/orders/{order_id}/status/'
# headers = {
#     'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjE0NzQ5LCJpYXQiOjE3MjkyMTQ0NDksImp0aSI6IjY1YTAzODc3NTU5NzRiODBhMGVhNDkxMGMzNjFkNjZlIiwidXNlcl9pZCI6Mn0.DxPbxqwjUpH81pxEzwGjTUjtQ1kodCAp0lE459bL81g',  # Используйте ваш токен
#     'Content-Type': 'application/json'
# }
# data = {
#     'status': 'Pending'  # Замените на нужный статус
# }
#
# response = requests.patch(url, headers=headers, json=data)
#
# if response.status_code == 200:
#     print("Статус заказа обновлен:", response.json())
# else:
#     print(f"Ошибка: {response.status_code} - {response.text}")