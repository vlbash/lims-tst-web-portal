# Заява про зміну уповноваженних осіб (Додаток 18) !!!!!!!!!!!!!!! Доделать !!!!!!!!!!!!!!!!!!

def test_5_lims_test_case_2_3(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

    app.first_application.create_sixth_application()

    app.first_application.notifications_and_license_terms_fourth(comment='Коментар тест')


    app.session.logout()