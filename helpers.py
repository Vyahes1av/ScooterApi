import allure
from faker import Faker
from data import CreatingCourierData


class TestDateHelper:
    @staticmethod
    @allure.step("Генерация тела запроса для регистрации курьера")
    def creating_body(random_login):
        body = CreatingCourierData.Creat_courier_random_body.copy()
        body['login'] = random_login
        return body

    @staticmethod
    @allure.step("Генерация тела запроса для авторизации курьера ")
    def login_body(random_login):
        body = CreatingCourierData.Creat_courier_random_body.copy()
        body['login'] = random_login
        return body