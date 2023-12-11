from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page_choice_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    choice_gitar = "(//a[@href='/product/A083568'])[3]"
    add_to_cart = "//a[@class='btn btn-default btn-block btn-product-orange ']"
    order = "(//a[contains(text(), 'Оформить заказ')])[2]"


    # Getters

    def get_choice_gitar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_gitar)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order)))

        # Action

    def click_choice_gitar(self):
        self.get_choice_gitar().click()
        print("Выбираем гитару")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Добавляем гитару в корзину")

    def click_order(self):
        self.get_order().click()
        print("Нажимаем на 'Оформить заказ'")

    # Methods

    def choice_product(self):

        self.get_current_url()
        self.click_choice_gitar()
        self.click_add_to_cart()
        self.click_order()




