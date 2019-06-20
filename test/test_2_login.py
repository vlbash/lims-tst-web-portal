
def test_2_login(app):
    app.session.login(password='111', path_to_key='/home/ps/MyFiles/projects/lims-tst-web-portal/tools/98745612_7878789898_DU180323123055.ZS2')
    app.session.logout()
