import allure
import pytest

from helpers import TestDateHelper
from api import ScooterApi
from data import CreatingCourierData


class TestCreatingCourier:

    @allure.title("Создание курьера с рандомными данными")
    @allure.description("Проверка создание/удаление нового курьера")
    def test_creating_courier(self, generate_random_login, delete_user):
        request = ScooterApi.creating_courier(TestDateHelper.creating_body(generate_random_login))

        assert request.status_code == 201 and request.text == '{"ok":true}'

    @allure.title("Создание курьера с одинаковым логином")
    @allure.description("Проверка что создание курьера с одинаковым логином выдает ошибку")
    def test_creating_identical_courier(self):
        request = ScooterApi.creating_courier(CreatingCourierData.Courier_body)

        assert request.status_code == 409 and request.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title("Создание курьера без логина")
    @allure.description("Проверка что создание курьера без логина выдает ошибку")
    def test_creating_courier_no_login(self):
        request = ScooterApi.creating_courier(CreatingCourierData.Creat_courier_body_is_password)
        assert request.status_code == 400 and request.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title("Удаление несущечтвующего курьера")
    @allure.description("Проверка что при попытке удалить несуществующего курьера ручка выдает ошибку")
    def test_delete_courier(self):
        request = ScooterApi.deleted_courier_2('{"id":3961304}')
        assert request.status_code == 400

