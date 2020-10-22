from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_registration(selenium):
    registration_page = RegistrationPage(selenium)
    registration_page.register('****', '*****', '****', 'test@gmail.com', '*****', '****', '****')
    login_page = LoginPage(selenium)
    login_page.login('****', '****')
