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

    # 7 активируем поле "Оберить файл"

    # driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").click()

    # time.sleep(3)

    # 8 прописываем путь к ключу

    # driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").keys_to_typing('https://drive.google.com/file/d/1Ply752FN5_xYbd8QSa0hlMVxPBn_4xBh/view?usp=sharing')

    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys('C:\98745612_7878789898_DU180323123055.ZS2')

    # 9 Активирую поле ПАРОЛЬ
    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()

    # 10 Ввожу пароль

    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys('111')

    # 11 нажимаю кнопку ВОЙТИ

    driver.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
    time.sleep(5)
    # 12 Нажимаю кнопку ПОГОДИТИСЬ

    driver.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()

    time.sleep(10)
'''

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//div [@class = "g"]')
        return len(inner_search_results) > 5

    with allure.step('Ожидаем что колличество результатов теста будет больше 5'):
        WebDriver(driver, 5, 0.5).until(check_results_count)

    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_element_by_xpath('//div [@class = "g"]')
        link = search_results[0].find_element_by_xpath('//a/h3')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверим корректность Title страницы'):
        assert driver.title == 'Тут должен быть заголовок который будет присутствовать на открываемой нами страничке, мы проверяем наличие на страничке этого заголовка'
'''

