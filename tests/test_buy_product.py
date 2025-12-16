import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

# Получаем абсолютный путь к корневой папке проекта (main_project)
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page

# На данном сайте авторизация проходит 1 раз

@pytest.mark.run(order=1)
def test_buy_product(set_up, set_group):
    options = Options()
    #options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Дополнительные опции для обхода капчи
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    # Блокируем уведомления и всплывающие окна
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Блокировать
        "profile.default_content_setting_values.popups": 2,         # Блокировать всплывающие
        "credentials_enable_service": False,                        # Отключить сохранение паролей
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # Дополнительные опции против всплывающих окон
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_enter_catalog()
    mp.select_products_1()
    mp.select_enter_catalog()
    mp.select_products_2()
    mp.select_enter_catalog()
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.enter_cart()
    cp.products_check()
    cp.cart_checkout_button()
    mp.make_screenshot()
    print("Finish test SUCCESS")
    driver.quit()