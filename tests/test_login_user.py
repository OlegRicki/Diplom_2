import pytest
import allure
import faker
from test_base.base_login import BaseLogin
from constants import Constants

constants = Constants()
fake = faker.Faker()


@allure.epic('Группа тестов на авторизацию пользователя')
class TestLoginUser:
    @allure.title('Тест на авторизацию пользователя, проверяем код ответа и наличие в ответе токенов')
    def test_login_user(self, create_new_test_user):
        base_login = BaseLogin()
        response = base_login.login(login=constants.TEST_EMAIL, password=constants.TEST_PASSWORD)
        assert response.status_code == 200
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()


    @allure.title('Негативный тест на авторизацию с неверными параметрами, проверяем код ответа')
    @pytest.mark.parametrize('login, password', [[fake.email(domain='example.ru'), fake.password()], ['', '']])
    def test_fail_login(self, login, password):
        base_login = BaseLogin()
        response = base_login.login(login=login, password=password)
        assert response.status_code == 401
