import allure
import pytest
import time


from api import ScooterApi
from data import OrderData

class TestCreatOrders:

    @pytest.mark.parametrize("colors", [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]), ([])])
    @allure.title("Создание заказа с разными данными")
    @allure.description("Проверка создания заказа с разными данными в 'color'")
    def test_creat_order_color(self, colors):
        order = OrderData.Order_creat.copy()
        order["color"] = colors
        response = ScooterApi.creat_order(order)

        assert response.status_code == 201

    @allure.title("id заказа")
    @allure.description("Проверка id заказа после его создания в ответе запроса")
    def test_creat_order_track(self):
        order = OrderData.Order_creat.copy()
        order["color"] = ["GREY"]
        response = ScooterApi.creat_order(order)

        assert "track" in response.json()

    @allure.title("Принять заказ курьером")
    @allure.description("Проверка запроса на принятие заказа курьером при передаче id заказа и курьера")
    def test_accept_order(self):
        order = OrderData.Order_creat.copy()
        order["color"] = ["GREY"]
        response_order = ScooterApi.creat_order(order)
        order_data = response_order.json()['track']
        order_id = f"{order_data}"
        courier_id = f"?courierId=396904"
        time.sleep(2)
        response = ScooterApi.accept_order(order_id, courier_id)
        time.sleep(2)
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title("Принять несуществующий заказ")
    @allure.description("Проверка запроса на принятие заказа с несуществующим id заказа")
    def test_accept_order_id_fail(self):
        order_id = "0"
        courier_id = f"?courierId=396904"
        response = ScooterApi.accept_order(order_id, courier_id)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Заказа с таким id не существует"}'

    @allure.title("Принять заказ несуществующим курьером")
    @allure.description("Проверка запросв на принятие заказа с несуществующим id курьера")
    def test_accept_courier_id_fail(self):
        order_id = "1"
        courier_id = f"?courierId=0"
        response = ScooterApi.accept_order(order_id, courier_id)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Курьера с таким id не существует"}'


