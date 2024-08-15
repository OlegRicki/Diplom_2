import allure
import pytest

from test_base.base_create_new_user import CreateNewUserBase
from constants import Constants
from expected_response import CREATE_NEW_USER_RESPONSE, FAIL_CREATE_NEW_USER_RESPONSE



@allure.epic('Группа тестов на создание нового пользователя')
class TestCreateNewUser:
    @allure.title('Тест на создание нового пользователя, проверяем код ответа')
    @pytest.mark.usefixtures("delete_test_user")
    def test_create_new_user(self, delete_test_user):
        email = Constants.TEST_EMAIL
        password = Constants.TEST_EMAIL
        user_name = Constants.TEST_NAME
        base_create_new_user = CreateNewUserBase()
        response = base_create_new_user.create_new_user(username=user_name, email=email, password=password)
        assert response.status_code == 200
        delete_test_user['token'] = response.json()['accessToken']


    @allure.title('Негативный тест на создание пользователя используя уже использованные данные,'
                  ' проверяем код ответа и текст ответа')
    def test_fail_create_new_user_ith_data_used(self, create_new_test_user):
        base_create_new_user = CreateNewUserBase()
        response = base_create_new_user.create_new_user(
            username=Constants.TEST_NAME, email=Constants.TEST_EMAIL, password=Constants.TEST_PASSWORD)
        assert response.status_code == 403
        assert response.json() == CREATE_NEW_USER_RESPONSE

    @allure.title('Негативный тест на создание пользователя, без обязательных полей')
    def test_fail_create_new_user_non_field(self):
        email = ''
        password = ''
        user_name = ''

        base_create_new_user = CreateNewUserBase()
        response = base_create_new_user.create_new_user(
            username=user_name, email=email, password=password)
        assert response.status_code == 403
        assert response.json() == FAIL_CREATE_NEW_USER_RESPONSE
