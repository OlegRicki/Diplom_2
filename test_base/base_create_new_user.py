import allure
from unittest import TestCase

import requests

from constants import Constants

constants = Constants()


class TestCreateNewUserBase:
    @allure.step('Отправить запрос на создание пользователя')
    def create_new_user(self, username: str, email: str, password: str):
        url = constants.BASE_API_URL + 'auth/register'
        response = requests.post(url, json={'email': email, 'password': password, 'name': username})
        return response
