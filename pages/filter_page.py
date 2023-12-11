from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    gitars = "(//a[@href='/category/gitary'])[2]"
    acoustics_git = "//div[contains(text(), 'Акустические гитары')]"
    form_factor_git = "(//label[contains(text(), 'дредноут')])[2]"
    orient_git = "//label[contains(text(), 'правосторонняя')]"
    number_string_git = "(//label[contains(text(), '6')])[4]"
    button_apply = "(//button[contains(text(), 'Применить')])[2]"
    show_option = "(//span[@role='presentation'])[1]"
    show_option_var = "//li[contains(text(), 'Сначала дорогие')]"

    # Getters

    def get_gitars(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gitars)))

    def get_acoustics_git(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.acoustics_git)))

    def get_form_factor_git(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.form_factor_git)))

    def get_orient_git(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.orient_git)))

    def get_number_string_git(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_string_git)))

    def get_button_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply)))

    def get_show_option(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_option)))

    def get_show_option_var(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_option_var)))


    # Action

    def click_gitars(self):
        self.get_gitars().click()
        print("Нажимаем на 'Гитары'")

    def click_acoustics_git(self):
        self.get_acoustics_git().click()
        print("Выбираем 'Акустические гитары'")

    def click_form_factor_git(self):
        self.get_form_factor_git().click()
        print("Выбираем форм-фактор гитары")

    def click_orient_git(self):
        self.get_orient_git().click()
        print("Выбираем ориентацию гитары")

    def click_number_string_git(self):
        self.get_number_string_git().click()
        print("Выбираем колличество струн гитары")

    def click_button_apply(self):
        self.get_button_apply().click()
        print("Нажимаем 'Применить'")

    def click_show_option(self):
        self.get_show_option().click()
        print("Нажимаем на фильтр 'Показать'")

    def click_show_option_var(self):
        self.get_show_option_var().click()
        print("Выбираем фильтра 'Сначала дорогие'")


    # Methods

    def filters(self):

        self.get_current_url()
        self.click_gitars()
        self.click_acoustics_git()
        self.click_form_factor_git()
        self.click_orient_git()
        self.click_number_string_git()
        self.click_button_apply()
        self.click_show_option()
        self.click_show_option_var()




