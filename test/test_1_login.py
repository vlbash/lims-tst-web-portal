from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_login():
    driver = WebDriver(executable_path='tools//chromedriver.exe')
    # 1 Переходим на страничку
    driver.get('http://lims-tst-web-portal.bitsoft.com.ua/')
    # 2 maximize window
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 3 нажимаем кнопку "Войти на портал"
    driver.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
    # 4 выбираем вариант файловый носитель
    driver.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
    # 5 открываем выпадающий список Центр сртификации ключей
    time.sleep(3)
    driver.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
    # 6 выбираем вариант "Центр сертифікації ключів "Україна" "
    driver.find_element_by_xpath("//option[contains(.,'Україна')]").click()
    # 7 прописываем путь к ключу
    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys('C:\98745612_7878789898_DU180323123055.ZS2')
    # 9 Активирую поле ПАРОЛЬ
    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
    # 10 Ввожу пароль
    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys('111')
    # 11 нажимаю кнопку ВОЙТИ
    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
    time.sleep(10)
    # 12 Нажимаю кнопку ПОГОДИТИСЬ
    driver.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()
    time.sleep(3)
    # 13 Проверяю наличие элемента (заголовок Портал Держликслужбы)
    driver.find_element_by_xpath("//div[@class='header-inner']/h1").click()

    # logout
    driver.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/div/div/span").click()
    driver.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/ul/li[3]/div/a/div/span").click()
    time.sleep(3)
    # Проверяю наличие эленмента (Заголовок)
    driver.find_element_by_xpath("//h1[contains(.,'Онлайн-подача та відслідковування')]")