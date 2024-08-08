import requests
from constants import Constants

constants = Constants()


class TestBaseLogin:

    def login(self, login: str, password: str):
        url = constants.BASE_API_URL + 'auth/login'
        response = requests.post(url, json={'email': login, 'password': password})
        return response
