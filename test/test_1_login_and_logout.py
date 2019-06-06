# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_1_login_and_logout(app):
    app.session.login()
    app.session.logout()


