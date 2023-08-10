from pages.auth_page import AuthPage
import pytest


@pytest.mark.parametrize("log_in,password_log_in",
                         [('jixewa9258@weizixu.com', 'Piratpiz25'), ('+7 966 711-02-79', 'Drondro2')],
                         ids=['valid_email and valid_password', 'valid_number and valid_password_number_login'])
def test_authorisation(web_browser, log_in, password_log_in):

    page = AuthPage(web_browser)
    page.login.send_keys(log_in)
    page.password.send_keys(password_log_in)
    page.btn.click()
    page.click_out.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()


# Тест авторизации в табе "Логин" по номеру телефона. Баг.
# Авторизация в табе "Логин" в требованиях должна быть по логину.
# Иначе какой смысл в этом табе если он дублирует таб "Номер телефона"
def test_authorisation_tab_login(web_browser, log_in='+79667110279', password_log_in='Drondro2'):

    page = AuthPage(web_browser)
    page.tab_login.click()
    page.login.send_keys(log_in)
    page.password.send_keys(password_log_in)
    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()
