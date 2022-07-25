from time import sleep

from pages.base_page import BasePage
from pages.url_list import Labirint
from pages.locators import StartLocators, AuthFormLocators
from selenium.webdriver import ActionChains
from pages.locators import HomeLocators
from selenium.webdriver.common.keys import Keys


# Классы определяют параметры Header, стартовой страницы сайта и страницы авторизации,
# свойства и функции поиска элементов на странице

class Headers(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.url = Labirint.start_url
        driver.get(self.url)

        self.notification_btn = driver.find_element(*StartLocators.notification_btn)
        self.notification_btn_popup_mess = driver.find_element(*StartLocators.notification_btn_popup_mess)
        self.my_lab_btn = driver.find_element(*StartLocators.my_lab_btn)
        self.my_lab_btn_popup_mess = driver.find_element(*StartLocators.my_lab_btn_popup_mess)
        self.put_order_btn = driver.find_element(*StartLocators.put_order_btn)
        self.put_order_btn_mess = driver.find_element(*StartLocators.put_order_btn_mess)
        self.cart_btn = driver.find_element(*StartLocators.cart_btn)
        self.cart_btn_mess = driver.find_element(*StartLocators.cart_btn_mess_indicator)

        # menu
        self.books_menu_link = driver.find_element(*StartLocators.books_menu_link)
        self.books_dropdown_menu = driver.find_element(*StartLocators.books_dropdown_menu)
        self.books_elements = driver.find_elements(*StartLocators.books_menu_elements)

        self.best_menu_link = driver.find_element(*StartLocators.best_menu_link)
        self.school_menu_link = driver.find_element(*StartLocators.school_menu_link)
        self.school_sub_menu_link = driver.find_element(*StartLocators.school_menu_link)
        self.school_dropdown_menu = driver.find_element(*StartLocators.school_dropdown_menu)
        self.games_menu_link = driver.find_element(*StartLocators.games_menu_link)
        self.games_dropdown_menu = driver.find_element(*StartLocators.games_dropdown_menu)
        self.office_menu_link = driver.find_element(*StartLocators.office_menu_link)
        self.office_menu_elements = driver.find_elements(*StartLocators.office_menu_elements)
        self.office_dropdown_menu = driver.find_element(*StartLocators.office_dropdown_menu)
        self.more_btn = driver.find_element(*StartLocators.more_btn)
        self.more_dropdown_menu = driver.find_element(*StartLocators.more_dropdown_menu)
        self.club_menu_link = driver.find_element(*StartLocators.club_menu_link)
        self.club_dropdown_menu = driver.find_element(*StartLocators.club_dropdown_menu)

        # additional menu links
        self.delivery_and_payment_link = driver.find_element(*StartLocators.delivery_and_payment_link)
        self.certificates_link = driver.find_element(*StartLocators.certificates_link)
        self.rating_link = driver.find_element(*StartLocators.rating_link)
        self.novelty_link = driver.find_element(*StartLocators.novelty_link)
        self.sale_link = driver.find_element(*StartLocators.sale_link)
        self.contact_link = driver.find_element(*StartLocators.contact_link)
        self.support_link = driver.find_element(*StartLocators.support_link)

        self.in_social_media_btn = driver.find_element(*StartLocators.in_social_media_btn)
        self.social_media_vk_link = driver.find_element(*StartLocators.social_media_vk_link)

        self.put_order_btn = driver.find_element(*StartLocators.put_order_btn)

    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def start_img_click(self):
        self.driver.find_element(*StartLocators.logo_img).click()

    def amount_menu_click(self, index: int):
        self.driver.find_elements(*StartLocators.main_menu_points)[index].click()
        sleep(3)

    def amount_school_click(self, index: int):
        self.driver.find_elements(*StartLocators.school_sub_menu)[index].click()
        sleep(3)

    def amount_menu_2_click(self, index: int):
        self.driver.find_elements(*StartLocators.main_menu_2_points)[index].click()
        sleep(3)

    def search_field_click(self, search_value):
        search_field = self.driver.find_element(*StartLocators.search_field)
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.send_keys(Keys.ENTER)


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.enter_btn = None

        super().__init__(driver, timeout)
        url = "https://www.labirint.ru/cabinet"
        self.driver.get(url)
        self.auth_form = driver.find_element(*AuthFormLocators.auth_form)
        self.close_btn = driver.find_element(*AuthFormLocators.close_btn)
        self.phone_num_field = driver.find_element(*AuthFormLocators.phone_num_field)
        self.enter_btn = driver.find_element(*AuthFormLocators.enter_btn)
        self.agreement_check_box = driver.find_element(*AuthFormLocators.agreement_check_box)

    def enter_phone_number(self, number: str):
        self.phone_num_field.clear()
        self.phone_num_field.send_keys(number)

    def another_ways_to_enter_bnt_click(self):
        self.another_ways_to_enter = self.driver.find_element(*AuthFormLocators.another_ways_to_enter)
        self.another_ways_to_enter.click()
        self.auth_social_links_box = self.driver.find_element(*AuthFormLocators.auth_social_links_box)
        self.vk_link = self.driver.find_element(*AuthFormLocators.vk_link)
        self.ok_link = self.driver.find_element(*AuthFormLocators.ok_link)
        self.mail_ru_link = self.driver.find_element(*AuthFormLocators.mail_ru_link)
        self.yandex_link = self.driver.find_element(*AuthFormLocators.yandex_link)
        self.gmail_link = self.driver.find_element(*AuthFormLocators.gmail_link)


class HomePage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://www.labirint.ru"
        self.driver.get(url)

        self.put_order_btn = driver.find_element(*HomeLocators.put_order_btn)

    def logo_img(self):
        return self.driver.find_element(*StartLocators.logo_img)


