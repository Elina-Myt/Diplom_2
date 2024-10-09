import pytest
import requests
import allure
import api_url
from helper import generate_user_creds

@allure.epic("Изменение данных пользователя")
class TestEditUserData:

    @allure.title('Изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize('edited_field', ['email', 'name', 'password'])
    def test_edit_user_data_success(self, user, edited_field):
        user_data, access_token = user
        new_creds = generate_user_creds()
        user_data[edited_field] = new_creds[edited_field]
        response = requests.patch(api_url.user_url, headers={"Authorization": access_token}, data=user_data)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'email' in response.json()['user']
        assert 'name' in response.json()['user']

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('edited_field', ['email', 'name', 'password'])
    def test_edit_user_data_failed(self, user, edited_field):
        user_data, access_token = user
        new_creds = generate_user_creds()
        user_data[edited_field] = new_creds[edited_field]
        response = requests.patch(api_url.user_url, data=user_data)

        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()["message"] == "You should be authorised"