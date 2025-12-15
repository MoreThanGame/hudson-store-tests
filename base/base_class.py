import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good WORD")

    def get_screenshot(self):
        date_now = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + date_now + '.png'
        self.driver.save_screenshot('main_project/screen/' + name_screenshot)

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good result")