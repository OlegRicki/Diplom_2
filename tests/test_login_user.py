import pytest
import allure
import faker
from test_base.base_login import TestBaseLogin
from constants import Constants

constants = Constants()
fake = faker.Faker()


class TestLoginUser:
    def test_login_user(self):
        base_login = TestBaseLogin()
        response = base_login.login(login=constants.TEST_EMAIL, password=constants.TEST_PASSWORD)
        assert response.status_code == 200
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @pytest.mark.parametrize('login, password', [[fake.email(domain='example.ru'), fake.password()], ['', '']])
    def test_fail_login(self, login, password):
        base_login = TestBaseLogin()
        response = base_login.login(login=login, password=password)
        assert response.status_code == 401
