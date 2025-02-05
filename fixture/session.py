import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 3 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 4 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 5 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 6 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 7 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 9 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 10 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 11 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(10)
        # 12 Нажимаю кнопку ПОГОДИТИСЬ
        wd.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()
        time.sleep(5)
        # 13 Проверяю наличие элемента (заголовок Портал Держликслужбы)
        wd.find_element_by_xpath("//div[@class='header-inner']/h1").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/div/div/span").click()
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/ul/li[3]/div/a/div/span").click()
        time.sleep(3)
        # Проверяю наличие эленмента (Заголовок)
        wd.find_element_by_xpath("//h1[contains(.,'Онлайн-подача та відслідковування')]")
