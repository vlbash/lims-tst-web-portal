
def test_lims_test_case_2_1(app):
    app.session.login(password='111',
                      path_to_key='/home/vbash/projects/lims-tst-web-portal/tools/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_first_application(pib="Ступка Богдан Сильвестрович",
                                         email="test@test.ua",
                                         phone_number="+380123456789",
                                         fax_number="+380123456 789",
                                         city="Дніпро",
                                         flat="13",
                                         street="Тестова вулиця",
                                         index="12345",
                                         number_national_account="12345",
                                         requisits_number_national_account="23456",
                                         number_foreign_account="34567",
                                         requisits_number_forein_account="45678",
                                         duns_number="56789")
    app.first_application.create_mpd(company_name='Тест',
                           phone_number='+380123456789',
                           email='test@test.ua',
                           fax_number='+380123456789',
                           city="Дніпро",
                           index='12345',
                           street='Тестова вулиця',
                           adress='Test',
                           building='13')
    app.first_application.contract_contractors(edrpou='12345678',
                                     name_contractor='Тест',
                                     adress='Тест')
    app.first_application.authorized_persons(person_name='Тест',
                                   person_middle_name='Тестович',
                                   person_last_name='Тестов',
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
    app.first_application.dossier_file(version='Тест досьє',
                             comment='Тест коментар',
                             date_to='19.04.2025',
                             path_to_file='/home/vbash/projects/lims-tst-web-portal/tools/masloy.png')
    app.first_application.completeness_check()
    app.first_application.notifications_and_license_terms(comment='Коментар тест')
#    app.first_application.submit_application(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
#                                   password='111')
    app.session.logout()
