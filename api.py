import allure
import requests
import urls


class ScooterApi:
    @staticmethod
    @allure.step("Создание курьера")
    def creating_courier(body):
        return requests.post(urls.Base_url + urls.Creating_courier, json=body)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(body):
        return requests.post(urls.Base_url + urls.Login_courier, data=body)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(urls.Base_url + urls.Delete_courier.format(id=courier_id))

    @staticmethod
    @allure.step("Создание заказа")
    def creat_order(order):
        return requests.post(urls.Base_url + urls.Orders, json=order)

    @staticmethod
    @allure.step("Получение списка заказов")
    def order_list():
        return requests.get(urls.Base_url + urls.Orders)

    @staticmethod
    @allure.step("Удаление курьера")
    def deleted_courier_2(id):
        return requests.delete(urls.Base_url + urls.Delete_courier, json=id)

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id, courier_id):
        return requests.put(urls.Base_url + urls.Orders_accept + order_id + courier_id)

    @staticmethod
    @allure.step("Получение заказа по номеру")
    def order_track(order_id):
        return requests.get(urls.Base_url + urls.Orders_track + order_id)

    @staticmethod
    @allure.step("Ошибка получения заказа")
    def order_track_not():
        return requests.get(urls.Base_url + urls.Orders_track)
