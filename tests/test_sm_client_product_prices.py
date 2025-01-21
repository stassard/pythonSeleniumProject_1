import allure
from pages.client_product_prices_page import ClientProductPricesPage
from pages.login_page import LoginPage
import pytest

@allure.feature("Smoke Suite for Client Product Prices Page")
class TestSmokeClientProductPricesPage:
    """Создание прайс-листа"""
    @allure.title("Create Client Product Prices")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.create_client_product_prices()


    """Прочитать информацию о прайс-листе и сравнить с данными из грида"""
    @allure.title("Read Client Product Prices")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_read_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.read_client_product_prices()


    """Редактирование прайс-листа"""
    @allure.title("Update Client Product Prices")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_update_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.update_client_product_prices()


    """Удаление прайс-листа через троеточие в гриде"""
    @allure.title("Delete Client Product Prices using Dots In Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_prices_from_three_dots_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.delete_client_product_prices_from_three_dots_grid()


    """Удаление прайс-листа через чекбокс в гриде"""
    @allure.title("Delete Client Product Prices using Checkbox in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_prices_from_checkbox_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.delete_client_product_prices_from_checkbox_grid()


    """Удаление 4х прайс-листов через чекбоксы в гриде"""
    @allure.title("Multiselection Deleting Client Product Prices using Checkboxes in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_4_client_product_prices_from_checkbox_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.delete_4_client_product_prices_from_checkbox_grid()


    """Удаление прайс-листа через Select All"""
    @allure.title("Delete Client Product Prices using Select All")
    @allure.severity("Critical")
    @pytest.mark.smoke
    # @pytest.mark.skip
    def test_select_all_delete_client_product_prices(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.select_all_delete_client_product_prices()


    """Удаление прайс-листа через карточку матрицы"""
    @allure.title("Delete Client Product Prices from Card")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_client_product_prices_from_card(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.delete_client_product_prices_from_card()


    """Рестор прайс-листа через троеточие в гриде"""
    @allure.title("Restore Client Product Prices using Dots in Grid")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_restore_client_product_prices_from_three_dots_grid(self, driver):
        lp = LoginPage(driver)
        lp.authorization()
        cppp = ClientProductPricesPage(driver)
        cppp.open_client_product_prices_dict()
        cppp.restore_client_product_prices_from_three_dots_grid()