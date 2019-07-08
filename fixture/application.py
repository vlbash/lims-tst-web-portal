from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.first_application import FirstApplicationHelper


class Application:

    def __init__(self):
        # self.wd = WebDriver(executable_path='tools//chromedriver.exe')
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.first_application = FirstApplicationHelper(self)

    def open_home_page(self):
        wd = self.wd
# Dev
        wd.get('http://lims-dev-web-portal.bitsoft.com.ua')

# Prod
#        wd.get('http://lims-web-portal.bitsoft.group/')

# Stage
#        wd.get('http://stage-lims-portal.bitsoft.group')

    def destroy(self):
        self.wd.quit()
