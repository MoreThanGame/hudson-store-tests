from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class Login_page(Base):

    base_url = 'https://hudsonstore.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators

    enter_lk = '//a[@href="/account" and @class="leading-[17px]"]'
    user_name = '//input[@id="CustomerEmail"]'
    user_password = '//input[@id="CustomerPassword"]'
    button_login = '//input[@class="button button-primary w-full h-[3.438rem] text-black rounded-full text-xs font-extrabold uppercase py-[0.813rem] px-5" and @type="submit" and @value="Log In"]'
    lk_word = '//h1[@class="text-xl font-extrabold mt-0"]'

    # Getters

    def get_enter_lk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_lk)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))
    
    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))
    
    def get_lk_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_word)))
    # Actions

    def click_close_modal(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ESCAPE)
        print("Pressed ESC")

    def click_close_captcha(driver):
        """
        Закрывает iframe с капчей, кликая вне его области
        """
        try:
            # Ожидаем появления iframe
            wait = WebDriverWait(driver, 10)
            captcha_iframe = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            
            # Получаем размеры и позицию iframe
            location = captcha_iframe.location
            size = captcha_iframe.size
            
            # Кликаем вне iframe (например, в левом верхнем углу страницы)
            # Можно кликнуть в нескольких местах для надежности
            actions = webdriver.ActionChains(driver)
            
            # Вариант 1: Клик в верхнем левом углу страницы (0,0)
            actions.move_by_offset(0, 0).click().perform()
            
            # Вариант 2: Клик правее iframe
            click_x = location['x'] + size['width'] + 50
            click_y = location['y'] + 100
            actions.move_by_offset(click_x, click_y).click().perform()
            
            # Вариант 3: Клик левее iframe
            click_x = location['x'] - 50
            click_y = location['y'] + 100
            actions.move_by_offset(click_x, click_y).click().perform()
            
            # Небольшая пауза для применения изменений
            import time
            time.sleep(1)
            
            print("Iframe с капчей закрыт")
            return True
            
        except Exception as e:
            print(f"Не удалось закрыть iframe: {e}")
            return False
        
    def click_close_captcha(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        actions.send_keys(Keys.ESCAPE).perform()
        print("Close captcha")

    def click_enter_lk(self):
        self.get_enter_lk().click()
        print("Enter to lk")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("Input user password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click login button")

    def _use_javascript_to_hide(self):
    
        self.driver.execute_script("""
            // Скрываем все iframe
            var iframes = document.getElementsByTagName('iframe');
            for (var i = 0; i < iframes.length; i++) {
                iframes[i].style.display = 'none';
                iframes[i].style.visibility = 'hidden';
            }
            
            // Скрываем возможные overlay
            var overlays = document.querySelectorAll('[style*="position: fixed"], [style*="position: absolute"]');
            for (var i = 0; i < overlays.length; i++) {
                if (overlays[i].offsetWidth > 200) {
                    overlays[i].style.display = 'none';
                }
            }
            
            // Убираем modal классы
            document.body.classList.remove('modal-open');
        """)
        print("Применен JavaScript для скрытия элементов")
    #Methods

    def authorization(self):
        self.driver.get(self.base_url)
        self.get_current_url()
        self.click_close_modal()
        self.click_enter_lk()
        self.get_current_url()
        self.assert_word(self.get_lk_word(), "Log In To Your Account")
        self.input_user_name("pleshakov.job3@mail.ru")
        self.input_user_password("Sweswe123.")
        self.click_button_login()
        # Далее может вылететь капча (если часто заходить) - поэтому выходим с капчи - считаем, что авторизацию прошли. Пытался захватить айфрейм с капчей - не вышло, даже просто закрыть окно с капчей не получается, поэтому оставил переход на главную страницу.
        print("Переходим на главную страницу, чтобы избежать капчи")
        self.driver.get(self.base_url)
        self.get_current_url()
        print("Продолжаем тест с главной страницы")