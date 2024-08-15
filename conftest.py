import pytest

from test_base.base_create_new_user import CreateNewUserBase
from tests.test_create_new_user import faker
from test_base.test_base import BaseTest
from constants import Constants

constants = Constants()


@pytest.fixture(scope='function')
def create_new_test_user():
    user_name = faker.user_name()
    test_email = constants.TEST_EMAIL
    test_password = constants.TEST_PASSWORD
    base_create_new_user = CreateNewUserBase()
    response = base_create_new_user.create_new_user(username=user_name, email=test_email, password=test_password)
    yield response
    BaseTest().delete_user(access_token=response.json().get('accessToken'))


@pytest.fixture(scope='function')
def delete_test_user():
    user_data = {}
    yield user_data
    if 'token' in user_data:
        BaseTest().delete_user(access_token=user_data['token'])
