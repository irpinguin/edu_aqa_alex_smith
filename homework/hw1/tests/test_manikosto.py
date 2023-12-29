import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pages.main_page import MainPage


# def test_route_product_order(browser):
#     mp = MainPage(browser)
#     mp.open_main_page()


# class TestExample:
#
#     def test_1(self, connect_to_db):          # Прокидываем фикстуру в тест и она выполнится перед тестом
#         print(connect_to_db)                  # Используем фикстуру, она вернет нам текст с подключением к БД
#
#     def test_2(self,generate_data):
#         login = generate_data["login"]        # Записываем в переменную сгенерированный логин
#         password = generate_data["password"]  # Записываем в переменную полученный логин
#         print(login, password)

# @pytest.mark.usefixtures("generate_data")       # Вызываем фикстуру над классом
# class TestExample:
#
#     def test_1(self):
#         print(self.login)                       # Сюда передастся логин
#         print(self.password)                    # А сюда пароль


@pytest.mark.usefixtures("get_driver")
class TestPage:

    def test_2(self):
        self.driver.get("https://irmag.ru")

