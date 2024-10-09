import pytest
from helper import register_user, delete_user, generate_user_creds, create_order


@pytest.fixture(scope='function')
def generate_user():
    creds = generate_user_creds()
    return creds


@pytest.fixture(scope='function')
def user(generate_user):
    response = register_user(generate_user)
    access_token = response.json()['accessToken']
    yield generate_user, access_token
    delete_user(access_token)


@pytest.fixture(scope='function')
def order(user):
    user_data, access_token = user
    create_order(access_token)