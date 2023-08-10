from pages.auth_page import AuthPage


def test_link_user_1_agreement(web_browser):

    page = AuthPage(web_browser)

    page.user_1_agreement.click()
    # переключение на новое окно
    web_browser.switch_to.window(web_browser.window_handles[1])

    # проверка, что открыто новое окно
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_user_2_agreement(web_browser):

    page = AuthPage(web_browser)
    page.user_2_agreement.click()
    # переключение на новое окно
    web_browser.switch_to.window(web_browser.window_handles[1])

    # проверка, что открыто новое окно
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_user_3_agreement(web_browser):

    page = AuthPage(web_browser)
    page.user_3_agreement.click()
    # переключение на новое окно
    web_browser.switch_to.window(web_browser.window_handles[1])

    # проверка, что открыта нужная ссылка
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_forgot_password(web_browser):

    page = AuthPage(web_browser)
    page.link_forgot_password.click()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id' \
           in page.get_current_url()


def test_link_vk(web_browser):
    page = AuthPage(web_browser)
    page.link_vk.click()
    # проверка, что открыта нужная ссылка
    assert 'https://id.vk.com/auth' in page.get_current_url()

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_ok(web_browser):
    page = AuthPage(web_browser)
    page.link_ok.click()

    # проверка, что открыта нужная ссылка
    assert 'https://connect.ok.ru/dk' in page.get_current_url()

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_mail_ru(web_browser):
    page = AuthPage(web_browser)
    page.link_mail_ru.click()

    # проверка, что открыта нужная ссылка
    assert 'https://connect.mail.ru/oauth/authorize' in page.get_current_url()

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()


def test_link_yandex_mail(web_browser):
    page = AuthPage(web_browser)
    page.link_yandex_mail.click()

    # проверка, что открыта нужная ссылка
    assert 'https://passport.yandex.ru/auth' in page.get_current_url()

    # переключение на основное окно
    web_browser.switch_to.window(web_browser.window_handles[0])

    # закрытие браузера
    web_browser.quit()
