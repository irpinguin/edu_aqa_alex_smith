import pytest
from pages.tmp_page import TmpPage


class BaseTest:

    tmp_page: TmpPage

    @pytest.fixture(autouse=True)
    # def setup(self, request, driver):
    #     request.cls.driver = driver
    #     request.cls.tmp_page = TmpPage(driver)
    def setup(self, request, get_browser):
        request.cls.driver = get_browser
        request.cls.tmp_page = TmpPage(get_browser)