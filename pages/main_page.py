from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.cart_page import Cart_page
from pages.login_page import Login_page
class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart_page = Cart_page(driver)
        self.login_page = Login_page(driver)

    # Locators

    enter_catalog = '//a[@href="/collections/men" and text()="Men"]'
    select_product_1 = '//a[@data-samitapbl-handle="armani-exchange-regular-fit-polo-shirt-with-contrasting-profiles-xm001394af16262u0002"]'
    choose_size_product_1 = '//label[@data-size="XS"]'
    select_product_2 = '//a[@data-samitapbl-handle="new-balance-suede-sneakers-327-u327wsa"]'
    choose_size_product_2 = '//label[@data-size="36"]'
    select_product_3 = '//a[@data-samitapbl-handle="vans-old-skool-sneakers-vn000d3hbka1"]'
    choose_size_product_3 = '//label[@data-size="42"]'
    add_to_cart_product = '//button[@id="ProductSubmitButton-template--25158413746443__product_page_form_GTWUBp"]'

    # Getters

    def get_enter_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_catalog)))
    
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_choose_size_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_product_1)))
    
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    
    def get_choose_size_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_product_2)))
    
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    
    def get_choose_size_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_product_3)))
    
    def get_add_to_cart_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product)))
    
    # Actions

    def click_enter_catalog(self):
        self.get_enter_catalog().click()
        print("Click enter product catalog")
    
    def click_product_1(self):
        self.get_select_product_1().click()
        self.get_choose_size_product_1().click()
        self.get_add_to_cart_product().click()
        print("Click select product 1")

    def click_product_2(self):
        self.get_select_product_2().click()
        self.get_choose_size_product_2().click()
        self.get_add_to_cart_product().click()
        print("Click select product 2")

    def click_product_3(self):
        self.get_select_product_3().click()
        self.get_choose_size_product_3().click()
        self.get_add_to_cart_product().click()
        print("Click select product 3")

    #Methods

    def select_enter_catalog(self):
        self.get_current_url()
        self.click_enter_catalog()

    def select_products_1(self):
        self.get_current_url()
        self.click_product_1()
        self.login_page.click_close_modal()
        self.cart_page.close_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_product_2()
        self.login_page.click_close_modal()
        self.cart_page.close_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_product_3()
        self.login_page.click_close_modal()
        self.cart_page.close_cart()

    def make_screenshot(self):
        self.get_screenshot()