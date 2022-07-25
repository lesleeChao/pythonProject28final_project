from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from tests.conftests import web_driver_desktop

from pages.locators import AuthFormLocators
from pages.pages import AuthPage
from settings import Settings


# 1
def test_auth_page(web_driver_desktop):
    """Тест проверяет открытие страницы авторизации"""
    page = AuthPage(web_driver_desktop, 5)
    assert page.get_relative_link() == "/cabinet"


# 2
def test_phone_num_field_empty(web_driver_desktop):
    """Тест проверяет активность кнопки авторизации с незаполненным полем ввода телефона"""
    page = AuthPage(web_driver_desktop, 5)
    page.phone_num_field.clear()
    assert page.enter_btn.get_attribute("disabled") == "true"


# 3
def test_phone_num_field(web_driver_desktop):
    """Тест проверяет активность кнопки авторизации с заполненным полем ввода телефона"""
    page = AuthPage(web_driver_desktop, 5)
    page.enter_phone_number(Settings.phone_number)
    assert page.enter_btn.get_attribute("disabled") is None


# 4
def test_phone_num_wrong(web_driver_desktop):
    """Тест проверяет, появляется ли справочное сообщение, когда введенный номер телефона неверен"""
    page = AuthPage(web_driver_desktop)
    page.enter_phone_number(Settings.phone_number_wrong)
    page.enter_btn.click()
    assert web_driver_desktop.find_element(*AuthFormLocators.service_unavailable_help_message).is_displayed() is True


# 5
def test_agreement_checkbox(web_driver_desktop):
    """Тест проверяет возможность авторизоваться при снятом флажке соглашения"""
    page = AuthPage(web_driver_desktop)
    page.enter_phone_number(Settings.phone_number)
    page.another_ways_to_enter_bnt_click()
    page.agreement_check_box.click()
    assert page.enter_btn.get_attribute("value") == "Необходимо принять соглашение" and \
           "disabled-block" in page.auth_social_links_box.get_attribute("class")


# 6
def test_auth_social_links(web_driver_desktop):
    """Тест проверяет корректность работы кнопки 'Другие способы входа' """
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    assert page.auth_social_links_box.is_displayed() is True


# 7
def test_close_btn(web_driver_desktop):
    """Тест проверяет корректную работу элемента управления типа "кнопка" с пиктограммой
    "x", служащий для закрытия окна страницы авторизации"""
    page = AuthPage(web_driver_desktop)
    page.close_btn.click()
    assert page.auth_form.is_displayed() is False


# 8
def test_link_opens_vk(web_driver_desktop):
    """ Тест проверяет открытие страницы авторизации через соцсеть ВК """
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.vk_link.click()
    assert "vk.com" in page.driver.current_url


# 9
def test_link_opens_ok(web_driver_desktop):
    """Тест проверяет открытие страницы авторизации через соцсеть Одноклассники"""
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.ok_link.click()
    assert "ok.ru" in page.driver.current_url


# 10
def test_link_opens_mail(web_driver_desktop):
    """Тест проверяет открытие страницы авторизации через mail.ru"""
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.mail_ru_link.click()
    assert "mail.ru" in page.driver.current_url


# 11
def test_link_opens_yandex(web_driver_desktop):
    """Тест проверяет открытие страницы авторизации через yandex.ru"""
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.yandex_link.click()
    assert "yandex.ru" in page.driver.current_url


# 12
def test_link_opens_gmail(web_driver_desktop):
    """Тест проверяет открытие страницы авторизации через gmail.com"""
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.gmail_link.click()
    assert "accounts.google.com" in page.driver.current_url


# 13
def test_authorisation_google(web_driver_desktop):
    """Тест проверяет авторизацию через gmail.com"""
    page = AuthPage(web_driver_desktop)
    page.another_ways_to_enter_bnt_click()
    page.gmail_link.click()
    page.driver.find_element(*AuthFormLocators.google_email_field).send_keys(Settings.valid_gmail)
    page.driver.find_element(*AuthFormLocators.google_email_passw_next_btn).click()
    password = WebDriverWait(web_driver_desktop, 5).until(
        ec.element_to_be_clickable(AuthFormLocators.google_password_field))
    password.send_keys(Settings.valid_pass)
    page.driver.find_element(*AuthFormLocators.google_email_passw_next_btn).click()
    ActionChains(web_driver_desktop).move_to_element(page.driver.find_element(*AuthFormLocators.my_lab_btn)).perform()
    assert page.driver.find_element(*AuthFormLocators.log_out_btn).is_displayed() is True