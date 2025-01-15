import allure
from pages.client_product_prices_page import ClientProductPricesPage
from pages.login_page import LoginPage
import pytest

@allure.feature("Smoke Suite for Client Product Prices Page")
class TestSmokeClientProductPricesPage:
    """Создание матрицы Клиент Продукт Цены"""
    @allure.title("Create Client Product Prices")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.create_client_product_prices()


    """Прочитать информацию о найденной матрице Клиент Продукт Цена и сравнить с данными из грида"""
    @allure.title("Read Client Product Prices")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_read_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.read_client_product_prices()
