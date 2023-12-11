from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.filter_page import Filter_page
from pages.login_page import Login_page

import pytest

from pages.main_page_choice_product import Main_page_choice_product
from pages.order_page import Order_page


def test_buy_product(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\User.WSA34411\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization()

    fp = Filter_page(driver)
    fp.filters()

    mp = Main_page_choice_product(driver)
    mp.choice_product()

    op = Order_page(driver)
    op.order()


