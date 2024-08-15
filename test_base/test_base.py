import allure
import requests
from constants import Constants

constants = Constants()


class BaseTest:
    @allure.step('Удалить юзера')
    def delete_user(self, access_token: str):
        url = constants.BASE_API_URL + 'auth/user'

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 202:
            pass
        else:
            raise Exception(response.status_code, response.text)
