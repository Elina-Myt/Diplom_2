import random
import string
import allure
import requests
import api_url


@allure.step('Генерация случайной строки')
def generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

@allure.step('Генерация случайных имен, паролей, почты')
def generate_user_creds(exclude_email=False, exclude_password=False, exclude_name=False):
    credentials = {}

    if not exclude_email:
        credentials['email'] = generate_random_string(10) + '@yandex.ru'

    if not exclude_password:
        credentials['password'] = generate_random_string(10)

    if not exclude_name:
        credentials['name'] = generate_random_string(10)

    return credentials


@allure.step('Регистрация пользователя')
def register_user(payload):
    response = requests.post(api_url.register_url, data=payload)
    return response


@allure.step('Удаление созданного пользователя')
def delete_user(access_token):
    requests.delete(api_url.user_url, headers={"Authorization": access_token})


@allure.step('Получение списка двух ингредиентов')
def ingredient_list():
    ingredient_list = []
    response = requests.get(api_url.ingredients_url)
    ingredient_list.append(response.json()['data'][0]['_id'])
    ingredient_list.append(response.json()['data'][1]['_id'])
    return ingredient_list


@allure.step('Создание заказа авторизованным пользователем')
def create_order(access_token):
    order = {'ingredients': ingredient_list()}
    response = requests.post(api_url.orders_url, headers={"Authorization": access_token}, data=order)
    return response