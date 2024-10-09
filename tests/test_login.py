import pytest
import requests
import allure
import api_url

@allure.epic("Логин пользователя")
class TestLoginUser:

    @allure.title('Авторизация существующего пользователя')
    def test_login_user_success(self, user):
        response = requests.post(api_url.login_url, data=user[0])

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        assert response.json()['user']['email'] == user[0]['email']
        assert response.json()['user']['name'] == user[0]['name']

    @allure.title('Авторизация пользователя с неверными логином и паролем')
    @pytest.mark.parametrize('wrong_field', ['email', 'password'])
    def test_login_user_fail(self, user, wrong_field):
        user[0][wrong_field] += user[0][wrong_field]
        response = requests.post(api_url.login_url, data=user[0])

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"