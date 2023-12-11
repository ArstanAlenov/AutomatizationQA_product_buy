from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):

    url = 'https://www.muztorg.ru/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    to_come_in_main_page = "(//a[@href='/site/get-login-form'])[2]"
    to_come_in_pass = "//a[@class='js-login-way']"
    email = "//input[@name='LoginForm[login]']"
    password = "//input[@type='password']"
    sign_in = "//button[@id='login-by-pass_submit-btn']"
    main_word = "(//a[@href='/user/change-auth'])[2]"

    # Getters

    def get_to_come_in_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_come_in_main_page)))

    def get_to_come_in_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_come_in_pass)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sign_in (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in)))

    def get_main_word (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_to_come_in_main_page(self):
        self.get_to_come_in_main_page().click()
        print("Нажмаем 'Войти'")

    def click_to_come_in_pass(self):
        self.get_to_come_in_pass().click()
        print("Нажимаем 'Войти с помощью пароля'")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Вводим логин")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Вводим пароль")

    def click_sign_in(self):
        self.get_sign_in().click()
        print("Нажимаем 'Войти'")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_to_come_in_main_page()
        self.click_to_come_in_pass()
        self.input_email("autotestingqa@mail.ru")
        self.input_password("SeleniuM1985")
        self.click_sign_in()
        self.assert_word(self.get_main_word(), 'Личный кабинет')




