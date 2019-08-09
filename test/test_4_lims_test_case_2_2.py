# ЗАЯВА ПРО ВНЕСЕННЯ ДО ЄДР ВІДОМОСТЕЙ ПРО МІСЦЕ ПРОВАДЖЕННЯ ГОСПОДАРСЬКОЇ ДІЯЛЬНОСТІ - ДОДАВАННЯ МПД(ВИРОБНИЦТВО)

def test_4_lims_test_case_2_2(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_second_application()

    app.first_application.create_mpd_second(company_name='4 - Тест',
                           phone_number='+380123456789',
                           email='test@test.ua',
                           fax_number='+380123456789',
                           city="Дніпро",
                           index='12345',
                           street='Тестова вулиця',
                           adress='Test',
                           building='13')

    app.first_application.authorized_persons_second(person_name='Тест',
                                             person_middle_name='Тестович',
                                             person_last_name='4 - Тестов',
                                             person_ipn='1234567890',
                                             person_birthday='13.12.1986',
                                             education='Тест універ',
                                             graduation_year='2004',
                                             diplom_number='АП1312',
                                             graduation_date='13.12.2004',
                                             speciality='Тест',
                                             work_expirience='95', contract_number='12345',
                                             order_number='23456',
                                             date_contract='14.12.2004',
                                             date_appointment='14.12.2004',
                                             position='Тест директор',
                                             contact_information='12345',
                                             comment='Тест коментар')

    app.first_application.dossier_file_second(version='4 - Тест досьє',
                             comment='Тест коментар',
                             date_to='19.04.2025',
                             path_to_file='C:/masloy.png')
    app.first_application.completeness_check()
    app.first_application.notifications_and_license_terms_second(comment='Коментар тест')
    app.first_application.submit_application(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                             password='111')
    app.session.logout()



