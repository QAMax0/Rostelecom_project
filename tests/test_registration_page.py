from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.registrazion_page import RegistrationPage
import pytest


def generate_string(num: int):
    # Функция-генератор определённого количества символов на ввод
    return "x1%D3" * num


"""Проверка регистрации с валидными данными полей ввода по требованиям"""


@pytest.mark.parametrize("name,surname,email_or_phone,password,password_confirm",
                         [('Бу', 'Абдулхадимирова', '+79667110271', 'Drondpo3', 'Drondpo3'),
                          ('Ядвигамирослава', 'Ар', '79122345624', 'DronDigi!k', 'DronDigi!k'),
                          ('Антон-Вячеслав-Николай-Костери', 'Доливо-Добровольский-Евдокимов', '+375287265286',
                           'KITERPOLiT1&PINPONGL', 'KITERPOLiT1&PINPONGL'),
                          ('Ян-г', 'Ри-', 'android98@mail.ru', '"ALbATROS3LNVSJFFD"', '"ALbATROS3LNVSJFFDF"')],
                         ids=["1) valid - (name - 2 символа кирилицей, surname - 15 символов кирилицей,"
                              " phone +7, password - 8 символов, password-confirm - повтор)",
                              "2) valid - (name - 15 символов кирилицей, surname - 2 символа кирилицей,"
                              " phone без +, password - 15 символов, password-confirm - повтор)",
                              "3) valid - (name - 30 символов кирилицей, surname - 30 символов кирилицей,"
                              " phone +375, password - 10 символов, password-confirm - повтор)",
                              "4) valid - (name - 2 символа кирилицей тире 1 символ кирилицей, "
                              "surname - 2 символа кирилицей тире, email, "
                              "password - 20 символов, password-confirm - повтор)"
                              ])
def test_registration(web_browser, name, surname, email_or_phone, password, password_confirm):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.name.send_keys(name)
    page.surname.send_keys(surname)
    page.email_or_phone.send_keys(email_or_phone)
    page.password.send_keys(password)
    page.password_confirm.send_keys(password_confirm)
    page.btn_register.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution' \
           in page.get_current_url()


"""Тесты на появление сообщения валидации под полями формы регистрации при невалидных данных"""

# Тест на появление сообщения валидации в поле "Имя"
@pytest.mark.parametrize("name", ['Б', 'Абдулхадимирова-Абд-Пап', '', 'В-', 'Абдурахмангаджи-Абдурахмангаджиь'],
                         ids=["1) no valid - 1 символ кирилицей",
                              "2) no valid - 21 символ кирилицей с двумя тире внутри",
                              "3) no valid - empty str",
                              "4) no valid - 1 символ кирилицей и тире",
                              "5) no valid - 31 символ кирилицей"])
def test_message_validation_name(web_browser, name):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.name.send_keys(name)
    page.name.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
           == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест на появление сообщения валидации в поле "Фамилия"
@pytest.mark.parametrize("surname", ['-', 'Mironov', ' ', '0', 'Абду рахмангаджи-Абдурах мангадж'],
                         ids=["1) no valid - 1 спецсимвол тире",
                              "2) no valid - 7 символов латиницей с заглавной буквой",
                              "3) no valid - пробел",
                              "4) no valid - ноль",
                              "5) no valid - 31 символ кирилицей"])
def test_message_validation_surname(web_browser, surname):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.surname.send_keys(surname)
    page.surname.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
           == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест на появление сообщения валидации в поле "E-mail или мобильный телефон". Ввод E-mail"
@pytest.mark.parametrize("email_or_phone", ['mir@', 'bittip.mail.ru', 'milton@kis', ' @mik.ru', ' @ .ru'],
                         ids=["1) no valid - без example.ru",
                              "2) no valid - без @",
                              "3) no valid - без .ru",
                              "4) no valid - пробел@mik.ru",
                              "5) no valid - пробел@пробел.ru"])
def test_message_validation_email(web_browser, email_or_phone):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.email_or_phone.send_keys(email_or_phone)
    page.email_or_phone.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
           == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

# Тест на появление сообщения валидации в поле "E-mail или мобильный телефон". Ввод номера телефона"
@pytest.mark.parametrize("email_or_phone", ['+7912453234', '23924', '+375-34789658', '0', 'fd&kfd(d)'],
                         ids=["1) no valid - без 1 цифры",
                              "2) no valid - 5 цифр",
                              "3) no valid - +375, тире и 8 цифр",
                              "4) no valid - 0 (1 цифра)",
                              "5) no valid - латинские буквы и спецсимволы"])
def test_message_validation_phone(web_browser, email_or_phone):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.email_or_phone.send_keys(email_or_phone)
    page.email_or_phone.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
           == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

# Тест на появление сообщения валидации в поле "Пароль". Ввод 7 символов. На 1 меньше минимума"
def test_message_validation_password_8simbols(web_browser, password='w3Eflds'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Длина пароля должна быть не менее 8 символов"

# Тест на появление сообщения валидации в поле "Пароль".
# Ввод кирилицы в пароле вместе с латинской заглавной буквой, цифрой, строчными латинскими буквами.
def test_message_validation_password_latin_letters(web_browser, password='w3Efldsоапавы'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Пароль должен содержать только латинские буквы"

# Тест на появление сообщения валидации в поле "Пароль". Ввод без строчной латинской буквы"
def test_message_validation_password_1_lowercase_letter(web_browser, password='I3EFLDTYR'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Пароль должен содержать хотя бы одну строчную букву"

# Тест на появление сообщения валидации в поле "Пароль". Ввод без заглавной латинской буквы"
def test_message_validation_password_1_capital_letter(web_browser, password='2ldlfdsffg'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Пароль должен содержать хотя бы одну заглавную букву"

# Тест на появление сообщения валидации в поле "Пароль". Ввод 21 валидного символа. Больше максимума в 20 символов."
def test_message_validation_password_20_simbols(web_browser, password='2ld!lfdsffgffdggdPuy1'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Длина пароля должна быть не более 20 символов"

# Тест на появление сообщения валидации в поле "Пароль". Ввод без 1 спецсимвола или 1 цифры."
def test_message_validation_password_1_special_character(web_browser, password='Gkfdbcktfnbarujqlbvc'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
           == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"

# Тест на появление сообщения валидации в поле "Подтверждение Пароля".
# Ввод разных паролей в поля "Пароль" и "Подтверждение пароля"
def test_message_validation_password_password_confirmation(web_browser,
                                                           password='FhgkffdnFD%D',
                                                           password_confirm='FhgkffdnFD%D2'):
    page = RegistrationPage(web_browser)
    page.click_register.click()
    page.password.send_keys(password)
    page.password_confirm.send_keys(password_confirm)
    page.password_confirm.send_keys(Keys.ENTER)
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
           == "Пароли не совпадают"
