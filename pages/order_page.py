from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators


    add_dop_product = "//a[contains(text(), 'Музыкальные курсы')]"     #в корзине добавляем доп. продукт
    course_git = "(//a[@data-role='cart-product-add'])[13]"            # добавляем курсы по игре на гитаре
    cont_registration = "//button[@class='button button-orange js-buy-btn']"   #нажимаем на кнопку "Продолжить оформление"

    # Getters

    def get_add_dop_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_dop_product)))

    def get_course_git(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.course_git)))

    def get_cont_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cont_registration)))

    # Action

    def click_add_dop_product(self):
        self.get_add_dop_product().click()
        print("Выбираем доп. продукт")

    def click_course_git(self):
        self.get_course_git().click()
        print("Выбираем курсы игры на гитаре")

    def click_cont_registration(self):
        self.get_cont_registration().click()
        print("Выбираем 'Продолжить оформление'")


    #Method

    def order(self):

        self.get_current_url()
        self.click_add_dop_product()
        self.click_course_git()
        self.click_cont_registration()

