
def test_1_login_and_logout(app):
    app.session.login()
    app.session.logout()
