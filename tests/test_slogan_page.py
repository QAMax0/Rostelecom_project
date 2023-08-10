from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage



def test_slogan(web_browser):

    page = AuthPage(web_browser)

    assert web_browser.find_element(By.XPATH, '//*[@id="page-left"]/div/div[2]/h2').text == "Личный кабинет"
    assert web_browser.find_element(By.XPATH, '//*[@id="page-left"]/div/div[2]/p').text\
           == "Персональный помощник в цифровом мире Ростелекома"
