import allure
import faker
import pytest

from test_base.base_create_new_user import TestCreateNewUserBase
from constants import Constants

constants = Constants()
faker = faker.Faker()


@allure.epic('Группа тестов на создание нового пользователя')
class TestCreateNewUser:
    @allure.title('Тест на создание нового пользователя, проверяем код ответа')
    @pytest.mark.usefixtures("delete_test_user")
    def test_create_new_user(self, delete_test_user):
        email = constants.TEST_EMAIL
        password = constants.TEST_EMAIL
        user_name = constants.TEST_NAME
        base_create_new_user = TestCreateNewUserBase()
        response = base_create_new_user.create_new_user(username=user_name, email=email, password=password)
        assert response.status_code == 200
        delete_test_user['token'] = response.json()['accessToken']


    @allure.title('Негативный тест на создание пользователя используя уже использованные данные,'
                  ' проверяем код ответа и текст ответа')
    def test_fail_create_new_user_ith_data_used(self, create_new_test_user):
        base_create_new_user = TestCreateNewUserBase()
        response = base_create_new_user.create_new_user(
            username=constants.TEST_NAME, email=constants.TEST_EMAIL, password=constants.TEST_PASSWORD)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': 'User already exists'}

    @allure.title('Негативный тест на создание пользователя, без обязательных полей')
    def test_fail_create_new_user_non_field(self):
        email = ''
        password = ''
        user_name = ''

        base_create_new_user = TestCreateNewUserBase()
        response = base_create_new_user.create_new_user(
            username=user_name, email=email, password=password)
        assert response.status_code == 403
        assert response.json() == {'message': 'Email, password and name are required fields', 'success': False}
