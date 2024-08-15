import allure

from test_base.base_change_user_data import BaseChangeUserData
from constants import Constants
from expected_response import UNAUTHORIZED_RESPONSE, get_success_user_response

constants = Constants()


@allure.epic('Группа тестов на изменение данных пользователя')
class TestChangeUserData:
    @allure.title('Тест на изменение данных профиля, с авторизацией, проверяем код ответа и текст сообщение')
    def test_change_user_data(self, create_new_test_user):
        change_user_data_api = BaseChangeUserData()
        access_token, refresh_token = change_user_data_api.login_get_tokens(login=constants.TEST_EMAIL,
                                                                            password=constants.TEST_PASSWORD)
        response, name = change_user_data_api.change_user_data(access_token=access_token)
        assert response.status_code == 200
        assert response.json() == get_success_user_response(name=name)

    @allure.title('Тест на изменение данных профиля без авторизации, проверяем код ответа и текст сообщения')
    def test_change_user_data_non_authorization(self):
        change_user_data_api = BaseChangeUserData()

        response = change_user_data_api.change_user_data_non_authorization()

        assert response.status_code == 401
        assert response.json() == UNAUTHORIZED_RESPONSE
