import allure
import requests
from constants import Constants
import faker

constants = Constants()
fake = faker.Faker()


class BaseChangeUserData:
    @allure.step('Авторизоваться и получить токены')
    def login_get_tokens(self, login: str, password: str):
        url = constants.BASE_API_URL + 'auth/login'
        response = requests.post(url, json={'email': login, 'password': password})
        access_token = response.json().get('accessToken')
        refresh_token = response.json().get('refreshToken')
        return access_token, refresh_token

    @allure.step('Изменить данные пользователя с авторизацией')
    def change_user_data(self, access_token):
        url = constants.BASE_API_URL + 'auth/user'
        new_name = fake.user_name()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }

        data = {
            "name": f"{new_name}"  # Новое имя
        }

        response = requests.patch(url, headers=headers, json=data)
        return response, new_name

    @allure.step('Изменить данные пользователя без авторизации')
    def change_user_data_non_authorization(self):
        url = constants.BASE_API_URL + 'auth/user'
        new_name = fake.user_name()

        data = {
            "name": f"{new_name}"
        }

        response = requests.patch(url, json=data)
        return response
