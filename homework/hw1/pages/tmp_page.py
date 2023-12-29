from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TmpPage(BasePage):

    # PAGE_URL = "https://irmag.ru/"
    PAGE_URL = "https://ya.ru/"
    MAIN_PAGE_SIGN_LOC = '//div[@id="index-last-blog-posts"]/h2'
    MAIN_PAGE_SIGN_VAL = 'Новые обзоры в блоге'

    def get_main_page_sign(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.MAIN_PAGE_SIGN_LOC)))

