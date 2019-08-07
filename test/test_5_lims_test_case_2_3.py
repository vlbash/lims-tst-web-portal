#ЗАЯВА ПРО ВНЕСЕННЯ ДО ЄДР ВІДОМОСТЕЙ ПРО МІСЦЕ ПРОВАДЖЕННЯ ГОСПОДАРСЬКОЇ ДІЯЛЬНОСТІ - ДОДАВАННЯ ІНФОРМАЦІЇ ПРО МПД(ВИРОБНИЦТВО)

def test_5_lims_test_case_2_3(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_third_application()

    app.first_application.change_mpd_third()

    app.first_application.notifications_and_license_terms_third(comment='Коментар тест')

    app.first_application.submit_application_third(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                             password='111')
    app.session.logout()
