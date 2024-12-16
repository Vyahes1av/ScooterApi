import allure
import pytest

from api import ScooterApi
from data import CreatingCourierData

class TestloginCourier:

    @allure.title("Авторизация курьера")
    @allure.description("Проверка успешной авторизации курьера")
    def test_login_courier(self):
        request = ScooterApi.login_courier(CreatingCourierData.Courier_body)

        assert request.status_code == 200 and request.text == '{"id":396904}'

    @allure.title("Авторизация курьера без логина")
    @allure.description("Проверка что запрос авторизации без логина выдает ошибку")
    def test_login_courier_no_login(self):
        request = ScooterApi.login_courier(CreatingCourierData.Creat_courier_body_is_password)

        assert request.status_code == 400 and request.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title("Авторизация несуществующего курьера")
    @allure.description("Проверка что запрос авторизации с несуществующеми данными выдает ошибку")
    def test_login_courier_non_existen(self):
        request = ScooterApi.login_courier(CreatingCourierData.Courier_non_existen)

        assert request.status_code == 404 and request.text == '{"code":404,"message":"Учетная запись не найдена"}'