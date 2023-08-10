from pages.base import WebPage
from pages.elements import WebElement


class RegistrationPage(WebPage):

    def __init__(self, web_driver, url=''):

        url = url if url else 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    click_register = WebElement(id="kc-register")
    name = WebElement(name="firstName")
    surname = WebElement(name="lastName")
    email_or_phone = WebElement(id="address")
    password = WebElement(id="password")
    password_confirm = WebElement(id="password-confirm")
    btn_register = WebElement(name="register")

