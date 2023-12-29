# Хранится драйвер
# сюда же универсальные методы: скриншоты, возврат урл, скролл и т.д.
import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    # Method asser sign
    def assert_sign(self, sign, result):
        value_sign = sign.text
        assert value_sign == result
        print("Sign value is OK")

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('./screen/' + name_screenshot)

    # Method assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Url is OK")