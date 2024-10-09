import requests
import allure
import api_url
from helper import ingredient_list

@allure.epic("Создание заказа")
class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_auth_success(self, user):
        user_data, access_token = user
        order = {'ingredients': ingredient_list()}
        response = requests.post(api_url.orders_url, headers={"Authorization": access_token}, data=order)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа неавторизованным авторизации')
    def test_create_order_without_auth_success(self):
        order = {'ingredients': ingredient_list()}
        response = requests.post(api_url.orders_url, data=order)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_fail(self):
        response = requests.post(api_url.orders_url, data={})

        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_incorrect_hash_ingredients_fail(self):
        order = {'ingredients': ['wrong_hash_ingredient']}
        response = requests.post(api_url.orders_url, data=order)

        assert response.status_code == 500
        assert response.reason == 'Internal Server Error'