from base.base_class import Base
import os
from dotenv import load_dotenv, find_dotenv
import allure
from utilities.logger import Logger


class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    load_dotenv(find_dotenv())

    # Locators
    button_login = "(//button[contains(@class,'prospace-button')])[1]"        # Кнопка ProSpace
    input_login_field = "//input[@type='text']"                               # Поле Логин
    input_password_field = "//input[@type='password']"                        # Поле Пароль
    button_signin = "//span[text()='Sign In']"                                # Кнопка Sign in
    header_of_promo_page = "//div[contains(text(),'Promo Portfolio')]"        # Заголовок страницы Промо Портфолио

    # Actions

    def get_main_word(self):
        return self.element_is_visible(self.header_of_promo_page)

    def input_login(self, user_name):
        return self.element_is_clickable(self.input_login_field).send_keys(user_name)

    def input_password(self, password):
        return self.element_is_clickable(self.input_password_field).send_keys(password)

    def click_button_login(self):
        return self.element_is_clickable(self.button_login).click()


    def click_button_signin(self):
        return self.element_is_clickable(self.button_signin).click()

    # Methods
    def authorization(self):
        """ Авторизация в системе"""
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(os.getenv("DEV_1"))
            self.driver.maximize_window()
            self.click_button_login()
            self.input_login(os.getenv("ADMIN_LOGIN"))
            self.input_password(os.getenv("ADMIN_PASSWORD"))
            self.click_button_signin()
            self.assert_word(self.get_main_word(), "Promo Portfolio")
            print("Успешная авторизация. Пользователь на странице Promo")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
