# ЗАЯВА ПРО ВНЕСЕННЯ ЗМІН ДО ЄДР У ЗВ’ЯЗКУ З ПРИПИНЕННЯМ ДІЯЛЬНОСТІ ЗА ПЕВНИМ МІСЦЕМ ПРОВАДЖЕННЯ - ВИДАЛЕННЯ МПД(ВИРОБНИЦТВО)

def test_5_lims_test_case_2_3(app):
    app.session.login(password='111',
                      path_to_key='/home/vbash/projects/lims-tst-web-portal/tools/98745612_7878789898_DU180323123055.ZS2')

    app.first_application.create_fourth_application()

    app.first_application.delete_mpd_fourth()

    app.first_application.notifications_and_license_terms_fourth(comment='Коментар тест')

    app.first_application.submit_application_third(path_to_key='/home/vbash/projects/lims-tst-web-portal/tools/98745612_7878789898_DU180323123055.ZS2',
                                             password='111')

    app.session.logout()
