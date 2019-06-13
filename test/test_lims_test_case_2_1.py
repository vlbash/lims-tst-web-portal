
def test_lims_test_case_2_1(app):
    app.session.login()
    app.session.create_first_application()
    app.session.create_mpd()
    app.session.contract_contractors()
    app.session.authorized_persons()
    app.session.dossier_file()
    app.session.completeness_check()
    app.session.notifications_and_license_terms()
    app.session.submit_application()

    app.session.logout()
