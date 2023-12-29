import random
import pytest
from base.base_test import BaseTest

class TestProfileFeature(BaseTest):

    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        # self.login_page.click_submit_button()

