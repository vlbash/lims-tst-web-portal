from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        # self.wd = WebDriver(executable_path='tools//chromedriver.exe')
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://lims-tst-web-portal.bitsoft.com.ua/')

    def destroy(self):
        self.wd.quit()
