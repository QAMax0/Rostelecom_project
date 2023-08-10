from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):

        url = url if url else 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    login = WebElement(id='username')
    password = WebElement(id='password')
    btn = WebElement(id='kc-login')
    click_out = WebElement(id='logout-btn')
    user_1_agreement = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/a')
    user_2_agreement = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[1]')
    user_3_agreement = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[2]')
    link_forgot_password = WebElement(xpath='//*[@id="forgot_password"]')
    link_vk = WebElement(id='oidc_vk')
    link_ok = WebElement(id='oidc_ok')
    link_mail_ru = WebElement(id='oidc_mail')
    link_yandex_mail = WebElement(id='oidc_ya')
    tab_login = WebElement(id="t-btn-tab-login")
