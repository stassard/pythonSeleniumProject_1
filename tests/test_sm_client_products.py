import allure
from pages.client_products_page import ClientProductsPage
from pages.login_page import LoginPage
import pytest

@allure.feature("Smoke Suite for Client Products Page")
class TestSmokeClientProductsPage:
    """Создание Клиента Продукта"""
    @allure.title("Create Client Products")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_client_products(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cpp = ClientProductsPage(driver)
        cpp.open_client_products_dict()
        cpp.create_client_product()