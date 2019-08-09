# Заява про анулювання ліцензії (Додаток 22)

def test_12_lims_test_case_2_10(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

    app.first_application.create_tenth_application()

    app.first_application.notifications_and_license_terms_tenth(comment='Коментар тест')

    app.first_application.submit_application_tenth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                             password='111')

    app.session.logout()
