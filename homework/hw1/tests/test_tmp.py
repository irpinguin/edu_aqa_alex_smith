import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_test import BaseTest


class TestSample(BaseTest):

    def test_1(self):
        self.tmp_page.open()
