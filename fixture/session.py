import time
# from selenium.webdriver import ActionChains

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
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

    def create_first_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

#        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про отримання ліцензії на провадження діяльності з виробництва лікарських засобів (промислового)» (додаток 2)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a").click()

        # Заповнюємо форму: Організаційно-правова форма* «460 Громадська організація»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Форма власності «40 Власність інших держав»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Прізвищеб ім'я по батькові керівника юридичної особи  «Ступка Богдан Сильвестрович»
        wd.find_element_by_xpath("//input[@id='OrgDirector']").send_keys("Ступка Богдан Сильвестрович")

        # Заповнюємо форму: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys("test@test.ua")

        # Заповнюємо форму: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys("+380123456789")

        # Заповнюємо форму: Номер факсу «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys("+380123456789")

        # Заповнюємо форму: Населений пункт* «Дніпропетровська область, Тернівка»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys("Дніпро")
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форму: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys("13")

        # Заповнюємо форму: Вулиця* (натискаємо синій квадрат з білим хрестиком посередині, зявляеться вікно додавання, у полі тип вулиці обераємо – проспект, у полі Назва вулиці пишемо «Тест» натискаємо кнопку СТВОРИТИ)
        wd.find_element_by_xpath("//button[@id='btn-street']").click()
        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/ul/li[2]/span").click()
        wd.find_element_by_xpath("//input[@id='Name']").send_keys("Тестова вулиця")
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Створити']").click()

        # Заповнюємо форму: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys("12345")

        # Заповнюємо форму: Номер рахунку в національній валюті «12345»
        wd.find_element_by_xpath("//input[@id='NationalAccount']").send_keys("12345")

        # Заповнюємо форму: Реквизити банку з рахунком в національній валюті «23456»
        wd.find_element_by_xpath("//input[@id='NationalBankRequisites']").send_keys("23456")

        # Заповнюємо форму: Номер рахунку в іноземній валюті «34567»
        wd.find_element_by_xpath("//input[@id='InternationalAccount']").send_keys("34567")

        # Заповнюємо форму: Реквизити банку з рахунком в іноземній валюті «45678»
        wd.find_element_by_xpath("//input[@id='InternationalBankRequisites']").send_keys("45678")

        # Заповнюємо форму: D-U-N-S номер (за наявності) «56789»
        wd.find_element_by_xpath("//input[@id='Duns']").send_keys("56789")
        time.sleep(2)
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")


    def create_mpd(self):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Натискаємо кнопку «Додати МПД» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення провадження діяльності: Найменування структурного підрозділу (або найменування юридичної особи):* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys('Тест')

        # Заповнюємо форми Створення провадження діяльності: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys('+380123456789')

        # Заповнюємо форми Створення провадження діяльності: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys('test@test.ua')

        # Заповнюємо форми Створення провадження діяльності: Номер факсу* «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys('+380123456789')

        # Заповнюємо форми Створення провадження діяльності: Населений пункт* «Дніпропетровська область, Дніпро»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys("Дніпро")
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форми Створення провадження діяльності: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys('12345')

        # Заповнюємо форми Створення провадження діяльності: Вулиця* (натискаємо синій квадрат з білим хрестиком посередині, зявляеться вікно додавання вулиці, у полі тип вулиці обераємо – проспект, у полі Назва вулиці пишемо «Тест» натискаємо кнопку СТВОРИТИ)
        wd.find_element_by_xpath("//button[@id='btn-street']").click()
        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/ul/li[2]/span").click()
        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[3]/input").send_keys('Тестова вулиця')
        time.sleep(2)
        wd.find_element_by_xpath("//input[@value='Створити']").click()

        # Заповнюємо форми Створення провадження діяльності: Адреса місця провадження діяльності (англійською)* «Test»
        wd.find_element_by_xpath("//input[@id='AdressEng']").send_keys('Test')

        # Заповнюємо форми Створення провадження діяльності: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys('13')

        time.sleep(2)
        # Обераємо чекбокс «Виробничі дільниці з переліком лікарських форм*»
        wd.find_element_by_xpath("//form[@id='editBranch']/div[3]/div/label").click()

        # Обераємо чекбокс «1. ВИРОБНИЧІ ОПЕРАЦІЇ - ЛІКАРСЬКІ ФОРМИ»
        wd.find_element_by_xpath("//div[@id='content-tree']/ul/li/div/label").click()
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def contract_contractors(self):
        wd = self.app.wd
        # Натискаємо кнопку «Контрактні контрагенти»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        # Натискаємо кнопку «Додати Контрактного контрагента» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення Контрактного контрагента: Тип контрагента* обираемо вариант «Контрактна лабораторія»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форми Створення Контрактного контрагента: ЄДРПОУ/ІПН* «12345678»(мінімальна кількість знаків 8 шт.)
        wd.find_element_by_xpath("//input[@id='Edrpou']").send_keys('12345678')

        # Заповнюємо форми Створення Контрактного контрагента: Найменування суб'єкта господарювання «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys('Тест')

        # Заповнюємо форми Створення Контрактного контрагента: Найменування, місце провадження діяльності* «Тест»
        wd.find_element_by_xpath("//input[@id='Address']").send_keys('Тест')

        # Заповнюємо форми Створення Контрактного контрагента: Оберіть МПД «Тест»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def authorized_persons(self):
        wd = self.app.wd

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        # Натискаємо кнопку «Додати уповноважену особу» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення уповноваженної особи: Ім'я* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys('Тест')

        # Заповнюємо форми Створення уповноваженної особи: По батькові* «Тестович»
        wd.find_element_by_xpath("//input[@id='MiddleName']").send_keys('Тестович')

        # Заповнюємо форми Створення уповноваженної особи: Прізвище* «Тестов»
        wd.find_element_by_xpath("//input[@id='LastName']").send_keys('Тестов')

        # Заповнюємо форми Створення уповноваженної особи: ІПН «» (10 цифр)
        wd.find_element_by_xpath("//input[@id='IPN']").send_keys('1234567890')

        # Заповнюємо форми Створення уповноваженної особи: Дата народження* «13.12.1986»
        wd.find_element_by_xpath("//input[@id='Birthday']").send_keys('13.12.1986')

        # Заповнюємо форми Створення уповноваженної особи: Найменування навчального закладу «»
        wd.find_element_by_xpath("//input[@id='EducationInstitution']").send_keys('Тест універ')

        # Заповнюємо форми Створення уповноваженної особи: Рік закінчення навчального закладу «2004»
        wd.find_element_by_xpath("//input[@id='YearOfGraduation']").send_keys('2004')

        # Заповнюємо форми Створення уповноваженної особи: Серія і номер диплому* «АП1312»
        wd.find_element_by_xpath("//input[@id='NumberOfDiploma']").send_keys('АП1312')

        # Заповнюємо форми Створення уповноваженної особи: Дата видачі диплому* «13.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfGraduation']").send_keys('13.12.2004')

        # Заповнюємо форми Створення уповноваженної особи: Спеціальність «Тест»
        wd.find_element_by_xpath("//input[@id='Speciality']").send_keys('Тест')

        # Заповнюємо форми Створення уповноваженної особи: Стаж роботи за фахом(місяців) «95»
        wd.find_element_by_xpath("//input[@id='WorkExperience']").send_keys('95')

        # Заповнюємо форми Створення уповноваженної особи: Номер трудового договору «12345»
        wd.find_element_by_xpath("//input[@id='NumberOfContract']").send_keys('12345')

        # Заповнюємо форми Створення уповноваженної особи: Номер наказу про покладання обов'язків 23456
        wd.find_element_by_xpath("//input[@id='OrderNumber']").send_keys('23456')

        # Заповнюємо форми Створення уповноваженної особи: Дата трудового договору «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfContract']").send_keys('14.12.2004')

        # Заповнюємо форми Створення уповноваженної особи: Дата наказу про покладання обовєязків «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfAppointment']").send_keys('14.12.2004')

        # Заповнюємо форми Створення уповноваженної особи: Посада «Тест директор»
        wd.find_element_by_xpath("//input[@id='NameOfPosition']").send_keys('Тест директор')

        # Заповнюємо форми Створення уповноваженної особи: Контактна інформація «12345»
        wd.find_element_by_xpath("//input[@id='ContactInformation']").send_keys('12345')

        # Заповнюємо форми Створення уповноваженної особи: Оберіть МПД «Тест»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label").click()

        # Заповнюємо форми Створення уповноваженної особи: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys('Тест коментар')

        # Клік
        wd.find_element_by_xpath("//div[@id='header-wrapper']").click()

        time.sleep(3)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def dossier_file(self):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        # Натискаємо кнопку «Додати досьє» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Редагування досьє: Назва/Версія «Тест досьє»
        wd.find_element_by_xpath("//input[@id='Version']").send_keys('Тест досьє')

        # Заповнюємо форми Редагування досьє: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys('Тест коментар')

        # Заповнюємо форми Редагування досьє: Дата з «01.01.2019»
        # wd.find_element_by_xpath("//input[@id='DateFrom']").send_keys('01.01.2019')

        # Заповнюємо форми Редагування досьє: Дата до «19.04.2025»
        wd.find_element_by_xpath("//input[@id='DateTo']").send_keys('19.04.2025')

        # Заповнюємо форми Редагування досьє: Оберіть МПД «Тест»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label").click()

        # Заповнюємо форми Редагування досьє: На формі «Додайте файли до картки досьє» натисувємо кнопку прикріпити файл (з ліва синій квадрат з білою скріпкою)
        # потім натискаємо кнопку збереження файлу (з права синій квадрат з зображенням дискети білого кольору)
        wd.find_element_by_xpath("//input[@id='files']").send_keys('C:/masloy.png')
        wd.find_element_by_xpath("//div[@id='uploadForm']/form/div[3]/button/i").click()

        #wd.find_element_by_xpath("//input[@id='files']").send_keys('Тест досье')

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def completeness_check(self):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[6]/i").click()

        # Перевірка комплектності поданих документів не виявила ніяких помилок
        wd.find_element_by_xpath("//p[contains(.,'Перевірка комплектності поданих документів не виявила ніяких помилок')]")

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[1]/i").click()

        time.sleep(2)

    def notifications_and_license_terms(self):
        wd = self.app.wd
        # Натискаємо кнопку «Досьє»

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[7]/i").click()

        # wd.find_element_by_css_selector(".icon-msg-envelope").click()
        # Обераємо наступні чекбокси: «Прошу за місцем/місцями провадження господарської діяльності провести перевірку матеріально-технічної бази,
        # кваліфікованого персоналу, а також умов щодо контролю якості лікарських засобів, що вироблятимуться»
        # Додатково до електронної форми бажаю отримати ліцензію на паперовому носії: «Нарочно»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[2]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[3]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[3]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[4]/label").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys('Коментар тест')

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(2)

    def submit_application(self):
        wd = self.app.wd
        # Натискаємо кнопку «Подання заяви»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[8]/i").click()

        # Натискаємо кнопку «Підписати і відправити заяву»
        wd.find_element_by_xpath("//a[@id='signButton']/span[2]").click()

        time.sleep(10)

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): Оберіть ЦСК «АЦСК ПАТ КБ «ПРИВАТБАНК
        wd.find_element_by_xpath("//div[@id='MainPageMenuPKeyPage']/div[2]/div[2]/div/div").click()

        # wd.find_element_by_xpath("//span[contains(.,'Україна')]").click()
        # //li[@class='select-item'][14]

        wd.find_element_by_xpath("//li[@class='select-item'][14]").click()

        #element = wd.find_element_by_xpath("//span[contains(.,'Україна')]").click
        #hover = ActionChains(wd).move_to_element(element)

        #hover.perform()

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): ОБЕРІТЬ ФАЙЛ З ОСОБИСТИМ КЛЮЧЕМ (ЗАЗВИЧАЙ З ІМ'ЯМ KEY-6.DAT) ТА ВКАЖІТЬ ПАРОЛЬ ЗАХИСТУ
        # Path
        wd.find_element_by_xpath("//input[@id='PKeyFileInput']").send_keys('C:/98745612_7878789898_DU180323123055.ZS2')
        # Пароль захисту ключа: «password»
        wd.find_element_by_xpath("//input[@id='PKeyPassword']").send_keys('111')
        # Натискаємо кнопку «Зчитати»
        wd.find_element_by_xpath("//button[@id='PKeyReadButton']").click()
        time.sleep(20)
        # ЩОБ ПІДПИСАТИ ТА ВІДПРАВИТИ ЗАЯВУ, ДАЙТЕ ЗГОДУ НА ПІДПИСАННЯ НАСТУПНИХ ФАЙЛІВ:
        # Обераємо Чекбокс  «Вибрати всі файли»
        wd.find_element_by_xpath("//div[@id='MainPageMenuPKeyPage']/div[4]/div[2]/label").click()

        # Натискаємо кнопку «Підписати»
        wd.find_element_by_xpath("//button[@id='SignDataButton']").click()

        time.sleep(10)
