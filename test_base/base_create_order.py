import allure
import requests
from constants import Constants

constants = Constants()


class BaseCreateOrder:
    @allure.step('Получить все ингридиенты')
    def get_data_ingredients(self):
        url = constants.BASE_API_URL + 'ingredients'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.json())

    @allure.step('Получить id ингридиента по имени')
    def get_id_ingredient_from_ingredients_by_name(self, ingredients, name_ingredient: str) -> str:
        ingredients = ingredients['data']
        for ingredient in ingredients:
            if ingredient['name'] == name_ingredient:
                return ingredient['_id']

    @allure.step('Отправить запрос на создание заказа')
    def create_order(self, bun, sauce, main):
        url = constants.BASE_API_URL + 'orders'
        json = {'ingredients': [bun, sauce, main]}
        response = requests.post(url, data=json)
        return response

    @allure.step('Отправить запрос на создание заказа без ингридиентов')
    def create_order_no_ingredients(self):
        url = constants.BASE_API_URL + 'orders'
        response = requests.post(url)
        return response

    @allure.step('Проверить что заказ успешный')
    def check_success_order(self, response):
        # Проверяем, что 'name', 'order' и 'success' присутствуют в response
        if 'name' in response and 'order' in response and 'number' in response['order'] and 'success' in response:
            return True
        else:
            return False

    @allure.step('Отправить запрос на создание заказа с авторизацией пользователя')
    def create_order_authorization_user(self, bun, sauce, main, access_token):
        url = constants.BASE_API_URL + 'orders'
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }
        json = {'ingredients': [bun, sauce, main]}
        response = requests.post(url, json=json, headers=headers)
        return response

