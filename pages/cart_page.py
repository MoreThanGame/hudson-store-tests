import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators

    close_cart_popup_window = '//button[@aria-label="Close Overlay Button"]'
    cart_order_button_popup = '//div[@id="cart-icon" and @href="/cart"]'
    cart_order_button_bag = '//a[@class="button button-inverse-pill !py-5 !mt-2.5 text-xs" and @href="/cart" and text()="View Your Bag"]'
    cart_checkout = '//button[@class="button button-pill w-full bg-primary h-[55px] text-sm mb-0.5 text-primary-button_text_color"]'
    check_name_product_1 = '//a[@class="font-extrabold uppercase text-xs mb-1.5 inline-block" and @title="ARMANI EXCHANGE"]'
    check_name_product_2 = '//a[@class="font-extrabold uppercase text-xs mb-1.5 inline-block" and @title="NEW BALANCE"]'
    check_name_product_3 = '//a[@class="font-extrabold uppercase text-xs mb-1.5 inline-block" and @title="VANS"]'
    
    # Getters

    def get_close_cart_popup_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_cart_popup_window)))
    
    def get_cart_order_button_popup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_order_button_popup)))
    
    def get_cart_order_button_bag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_order_button_bag)))
    
    def get_cart_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_checkout)))    
    
    def get_check_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_name_product_1)))    
    
    def get_check_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_name_product_2)))    
    
    def get_check_name_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_name_product_3)))    
    
    # Actions

    def close_overlay_widget(self):
        """Закрывает мешающий виджет через JavaScript"""
    try:
        self.driver.execute_script("""
            // Ищем и скрываем виджет hc-widget
            var widget = document.getElementById('hc-widget');
            if (widget) {
                widget.style.display = 'none';
                widget.style.visibility = 'hidden';
            }
            
            // Также скрываем другие возможные оверлеи
            var overlays = document.querySelectorAll('[style*="position: fixed"], [style*="position: absolute"]');
            overlays.forEach(function(el) {
                if (el.offsetWidth > 100 && el.offsetHeight > 100) {
                    el.style.display = 'none';
                }
            });
        """)
        print("Виджет hc-widget закрыт через JavaScript")
    except Exception as e:
        print(f"Не удалось закрыть виджет: {e}")

    def click_close_cart_popup_window(self):
        self.get_close_cart_popup_window().click()
        print("Click close cart popup window")

    def click_cart_order_button(self):
        self.close_overlay_widget()
        time.sleep(1)
        self.get_cart_order_button_popup().click()
        self.get_cart_order_button_bag().click()
        print("Enter cart")

    def click_cart_checkout(self):
        self.get_cart_checkout().click()
        print("Click cart checkout")

    def products_check_1(self):
        element_1 = self.get_check_name_product_1()
        success_test_check_product_1 = element_1.text
        assert success_test_check_product_1 == "ARMANI EXCHANGE"
        print("Test check product 1 OK")

    def products_check_2(self):
        element_2 = self.get_check_name_product_2()
        success_test_check_product_2 = element_2.text
        assert success_test_check_product_2 == "NEW BALANCE"
        print("Test check product 2 OK")

    def products_check_3(self):
        element_3 = self.get_check_name_product_3()
        success_test_check_product_3 = element_3.text
        assert success_test_check_product_3 == "VANS"
        print("Test check product 3 OK")

    #Methods

    def enter_cart(self):
        self.click_cart_order_button()

    def close_cart(self):
        self.click_close_cart_popup_window()

    def cart_checkout_button(self):
        self.click_cart_checkout()

    def products_check(self):
        self.products_check_1()
        self.products_check_2()
        self.products_check_3()
        print("Name test success")
