import pytest
import allure
from helper import register_user, delete_user

@allure.epic("Создание пользователя")
class TestCreateUser:

    @allure.title('Создание нового пользователя')
    def test_create_new_user(self, generate_user):
        creds = generate_user
        response = register_user(creds)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        assert response.json()['user']['email'] == creds['email']
        assert response.json()['user']['name'] == creds['name']

        access_token = response.json()['accessToken']
        delete_user(access_token)

    @allure.title('Создание пользователя, который существует')
    def test_create_existed_user(self, generate_user):
        response_1 = register_user(generate_user)
        response_2 = register_user(generate_user)

        assert response_2.status_code == 403
        assert response_2.reason == 'Forbidden'
        assert response_2.json()["success"] is False
        assert response_2.json()["message"] == "User already exists"

        access_token = response_1.json()['accessToken']
        delete_user(access_token)

    @allure.title('Создание пользователя, когда нет одного из полей')
    @pytest.mark.parametrize('empty_field', ['email', 'name', 'password'])


    def test_create_user_with_empty_field(self, empty_field, generate_user):
        creds = generate_user
        del creds[empty_field]
        response = register_user(generate_user)
        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"