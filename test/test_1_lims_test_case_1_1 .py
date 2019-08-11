# Login and logout

def test_1_lims_test_case_1_1(app):
    app.session.login(password='111', path_to_key='/home/vbash/projects/lims-tst-web-portal/tools/98745612_7878789898_DU180323123055.ZS2')
    app.session.logout()


