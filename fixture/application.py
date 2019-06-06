from selenium.webdriver.chrome.webdriver import WebDriver
import time


class Application:

    def __init__(self):
        self.wd = WebDriver(executable_path='tools//chromedriver.exe')
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://lims-tst-web-portal.bitsoft.com.ua/')

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/div/div/span").click()
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/ul/li[3]/div/a/div/span").click()
        time.sleep(3)
        # Проверяю наличие эленмента (Заголовок)
        wd.find_element_by_xpath("//h1[contains(.,'Онлайн-подача та відслідковування')]")

    def login(self):
        wd = self.wd
        self.open_home_page()
        # 3 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 4 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 5 открываем выпадающий список Центр сртификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 6 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 7 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            'C:/98745612_7878789898_DU180323123055.ZS2')
        # 9 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 10 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            '111')
        # 11 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(10)
        # 12 Нажимаю кнопку ПОГОДИТИСЬ
        wd.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()
        time.sleep(3)
        # 13 Проверяю наличие элемента (заголовок Портал Держликслужбы)
        wd.find_element_by_xpath("//div[@class='header-inner']/h1").click()

    def destroy(self):
        self.wd.quit
