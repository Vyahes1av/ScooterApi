import allure
import pytest

from api import ScooterApi
from data import OrderData


class TestOrderList:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка что запрос выдает список созданных заказов")
    def test_list_order(self):
        response = ScooterApi.order_list()

        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказа по id")
    @allure.description("Проверка создание заказа и его получение его по id")
    def test_track_order(self):
        order = OrderData.Order_creat.copy()
        order["color"] = ["GREY"]
        response_order = ScooterApi.creat_order(order)
        order_data = response_order.json()['track']
        order_id = f"{order_data}"
        response = ScooterApi.order_track(order_id)
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title("Несуществующий id заказа")
    @allure.description("Проверка ошибки запроcа заказа по несуществующему id")
    def test_track_false_order(self):

        response = ScooterApi.order_track("999999")
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Заказ не найден"}'

    @allure.title("Запрос заказа без id")
    @allure.description("Проверка запроса заказа без id")
    def test_track_false_order_not(self):
        response = ScooterApi.order_track_not()
        assert response.status_code == 400 and response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'