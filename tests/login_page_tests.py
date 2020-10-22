from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest

@pytest.mark.parametrize("username,password", [("*****", "****"), ("****", "****"), ("****", "*****")])
def test_login(selenium, username, password):
    login_page = LoginPage(selenium)
    login_page.login(username, password)
    main_page = MainPage(selenium)

