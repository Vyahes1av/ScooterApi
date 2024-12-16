
import random
import string

import allure
import pytest

from api import ScooterApi
from helpers import TestDateHelper


@pytest.fixture(scope="session")
@allure.step("Генерация случайного логина")
def generate_random_login():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(8))


@pytest.fixture(scope="function")
@allure.step("Создание нового пользователя и удаление его")
def delete_user(generate_random_login):
        yield
        login_response = ScooterApi.login_courier(TestDateHelper.login_body(generate_random_login))
        user_id = login_response.json()['id']
        ScooterApi.delete_courier(user_id)

@pytest.fixture(scope="function")
def creat_and_delete_user(generate_random_login, delete_user):
         ScooterApi.creating_courier(TestDateHelper.creating_body(generate_random_login))
         yield
