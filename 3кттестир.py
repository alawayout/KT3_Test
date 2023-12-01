import json

import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, json=data)
            elif request_type == 'PUT':
                response = requests.put(url, json=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True
        return response

    def get(self, endpoint, endpoint_id, expected_error=True):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id='', body=None):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body, expected_error=True)
        return response.json()

    def delete(self, endpoint, endpoint_id=''):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()['message']


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)

data = {
    "id": 3,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2023-10-10T09:16:16.448Z",
    "status": "placed",
    "complete": False
}

user_data = {
    'id': 2,
    'username': "Kirill",
    'firstName': "Kirill",
    'lastName': "Boremskiy",
    'email': "mail@.04.ru",
    'password': "123456789",
    'phone': "89999999999",
    'userStatus': 0
  }

# push_order = base_request.post('store', 'order', data) #Добавлениу заказа

# base_request.delete('store/order', 3) #удаление заказа

# store_info = base_request.get('store', 'inventory') #получение информации о списке товаров
# pprint.pprint(store_info)

# result = base_request.get('store/order', 3)   #получение информации о заказе
# pprint.pprint(result)

# user = base_request.post('user', body=user_data) #Добавление пользователя
# pprint.pprint(user)

# user = base_request.put('user', 'Kirill', user_data) #Изменение пользователя
# pprint.pprint(user)

# user2 = base_request.get('user', 'Kirill') #Получение информации о пользователе
# pprint.pprint(user2)

# delete = base_request.delete('user', 'Kirill') #Удаление пользователя
# print(delete)