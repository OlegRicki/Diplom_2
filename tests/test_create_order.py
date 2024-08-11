import allure
from test_base.base_create_order import BaseCreateOrder


@allure.epic('Группа тестов на создание заказа')
class TestCreateOrder:
    @allure.title('Тест создать заказ без авторизации, проверяем код ответа и текст ответа ')
    def test_create_order_authorization_false(self):
        base_create_order = BaseCreateOrder()
        ingredients = base_create_order.get_data_ingredients()
        bun = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Флюорисцентная булка')
        sauce = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Соус Spicy-x')
        main = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Мясо бессмертных моллюсков Protostomia')
        response = base_create_order.create_order(bun, sauce, main)
        assert response.status_code == 200
        response = response.json()
        assert base_create_order.check_success_order(response=response)

    def test_create_order_authorization_true(self):
        base_create_order = BaseCreateOrder()
        ingredients = base_create_order.get_data_ingredients()
        bun = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Флюорисцентная булка')
        sauce = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Соус Spicy-x')
        main = base_create_order.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Мясо бессмертных моллюсков Protostomia')
        response = base_create_order.create_order_authorization_user(bun, sauce, main)
        assert response.status_code == 200
        response = response.json()
        assert base_create_order.check_success_order(response=response)

    @allure.title('Негативный тест на создание заказа без ингридиентов, проверяем код ответа и текст ответа')
    def test_fail_create_order_no_ingredients(self):
        base_create_order = BaseCreateOrder()
        response = base_create_order.create_order_no_ingredients()
        assert response.status_code == 400
        assert response.json() == {'success': False, 'message': "Ingredient ids must be provided"}

    @allure.title('Негативный тест на создание заказа с невалидным хэшем, проверяем код ответа')
    def test_fail_create_order_invalid_hash(self):
        base_create_order = BaseCreateOrder()
        bun = 'er'
        sauce = 'df'
        main = 'df'
        response = base_create_order.create_order(bun, sauce, main)
        assert response.status_code == 500
