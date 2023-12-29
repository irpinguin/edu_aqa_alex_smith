# test_open_home_page.py

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_home_page(browser):
    browser.get("https://irmag.ru")
    assert browser.title == "Интернет-магазин IRMAG.RU — доставка по Иркутску, области и всей России косметики, парфюмерии, бытовой химии, товаров для дома и семьи."
