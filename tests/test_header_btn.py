# -*- encoding=utf8 -*-
from tests.conftests import web_driver_desktop

import pytest
from pages.pages import Headers
from pages.locators import StartLocators
from pages.url_list import Labirint


# 1
@pytest.mark.smoke
@pytest.mark.positive
def test_click_logo(web_driver_desktop):
    """Тест проверяет клик в header по логотипу и перезагрузку главной страницы"""

    page = Headers(web_driver_desktop)
    page.start_img_click()
    assert page.get_relative_link() == '/', 'Transition error'


# 2
@pytest.mark.smoke
@pytest.mark.positive
def test_displayed_notification(web_driver_desktop):
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Сообщение' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.notification_btn)
    assert page.notification_btn_popup_mess.is_displayed() is True


# 3
@pytest.mark.smoke
@pytest.mark.positive
def test_displayed_my_lab(web_driver_desktop):
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Мой Лаб' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.my_lab_btn)
    assert page.my_lab_btn_popup_mess.is_displayed() is True


# 4
@pytest.mark.smoke
@pytest.mark.positive
def test_display_putorder(web_driver_desktop):
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Отложено' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.put_order_btn)
    assert page.put_order_btn_mess.is_displayed() is True


# 5
@pytest.mark.smoke
@pytest.mark.positive
def test_displayed_card(web_driver_desktop):
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Корзина' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.cart_btn)
    assert "have-dropdown-selected" in page.cart_btn_mess.get_attribute("class")


# 6
@pytest.mark.smoke
@pytest.mark.positive
def test_href_attribute(web_driver_desktop):
    """Тест проверяет наличие ссылок на кнопках 'Сообщения', 'Мой лаб',
    'Отложено' и 'Корзина'"""
    page = Headers(web_driver_desktop)
    assert page.notification_btn.get_attribute("href") and page.my_lab_btn.get_attribute("href") \
           and page.put_order_btn.get_attribute("href") and page.cart_btn.get_attribute("href") != ""


# 7
@pytest.mark.smoke
@pytest.mark.positive
def test_click_menu_1(web_driver_desktop):
    """Тест проверяет кликабельность меню в Header по кнопкам "Книги", "Главное 2022",
    "Школа", "Игрушки", "Канцтовары", и переход на соответствующие страницы"""

    page = Headers(web_driver_desktop)

    for index in range(len(Labirint.main_menu_urls_1)):
        page.amount_menu_click(index)
        assert page.get_relative_link() in Labirint.main_menu_urls_1, f'Transition {index} error'
        page.get_url(page.url)


# 8
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_books(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Книги' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.books_menu_link)
    assert page.books_dropdown_menu.is_displayed() is True, \
        'Error, the list is not displayed'


# 9
@pytest.mark.smoke
@pytest.mark.positive
def test_background_color_menu_books(web_driver_desktop):
    """Тест проверяет изменение цвета у элементов выпадающего списка кнопки
    'Книги' при наведении на них указателя мыши"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.books_menu_link)
    menu_elements = page.books_elements
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


# 10
@pytest.mark.smoke
@pytest.mark.positive
def click_books_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике на кнопку 'Книги'"""
    page = Headers(web_driver_desktop)

    page.books_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_book, "Error URL"


# 11
@pytest.mark.smoke
@pytest.mark.positive
def test_click_best_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Главное 2022' """
    page = Headers(web_driver_desktop)

    page.best_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_best, "Error URL"


# 12
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_school(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Школа' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.school_menu_link)
    assert page.school_dropdown_menu.is_displayed() is True, 'Error, the list is not displayed'


# 13
@pytest.mark.smoke
@pytest.mark.positive
def test_click_school_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Школа' """
    page = Headers(web_driver_desktop)

    page.school_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_school, "Error URL"


# 14
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_games(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Игрушки' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.games_menu_link)
    assert page.games_dropdown_menu.is_displayed() is True


# 15
@pytest.mark.smoke
@pytest.mark.positive
def test_click_games_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Игрушки' """
    page = Headers(web_driver_desktop)

    page.games_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_games, "Error URL"


# 16
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_office(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Канцтовары' в Header"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.office_menu_link)
    assert page.office_dropdown_menu.is_displayed() is True


# 17
@pytest.mark.smoke
@pytest.mark.positive
def test_click_office_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Канцтовары' """
    page = Headers(web_driver_desktop)

    page.office_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_office, "Error URL"


# 18
@pytest.mark.smoke
@pytest.mark.positive
def test_background_color_menu_office(web_driver_desktop):
    """Тест проверяет изменение цвета у элементов выпадающего списка кнопки
    'Канцтовары' при наведении на них указателя мыши"""
    page = Headers(web_driver_desktop)
    page.move_to_element(page.office_menu_link)
    menu_elements = page.office_menu_elements
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


# 19
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_more_btn(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Ещё' в Header"""
    page = Headers(web_driver_desktop, 5)
    page.move_to_element(page.more_btn)
    assert page.more_dropdown_menu.is_displayed() is True


# 20
@pytest.mark.smoke
@pytest.mark.positive
def test_background_color_menu_more(web_driver_desktop):
    """Тест проверяет изменение цвета у элементов выпадающего списка кнопки
    'Ещё' при наведении на них указателя мыши"""
    page = Headers(web_driver_desktop, 5)
    page.move_to_element(page.more_btn)
    menu_elements = page.driver.find_elements(*StartLocators.more_menu_elements)
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


# 21
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_club_btn(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'Клуб' в Header"""
    page = Headers(web_driver_desktop, 5)
    page.move_to_element(page.club_menu_link)
    assert page.club_dropdown_menu.is_displayed() is True


# 22
@pytest.mark.smoke
@pytest.mark.positive
def test_click_club_btn(web_driver_desktop):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Клуб' """
    page = Headers(web_driver_desktop)

    page.club_menu_link.click()
    assert page.get_relative_link() == Labirint.btn_club, "Error URL"


# 23
@pytest.mark.smoke
@pytest.mark.positive
def test_main_menu_start_page(web_driver_desktop):
    """Тест проверяет кликабельность меню по кнопкам "Доставка и оплата, 'Сертификаты', 'Рейтинги',
    'Новинки', 'Скидки' и переход на соответствующие страницы меню"""

    page = Headers(web_driver_desktop, 5)

    # Перебор в цикле пунктов главного меню
    for index in range(len(Labirint.main_menu_urls_2)):
        page.amount_menu_2_click(index)
        assert page.get_current_url() in Labirint.main_menu_urls_2[index], f'Transition {index} error'
        # get_current_url

        page.get_url(page.url)


# 24
@pytest.mark.smoke
@pytest.mark.positive
def test_dropdown_menu_social_media_btn(web_driver_desktop):
    """Тест проверяет появление выпадающего списка при наведении на кнопку 'в соцсетях' в Header"""
    page = Headers(web_driver_desktop, 5)
    page.move_to_element(page.in_social_media_btn)
    assert page.social_media_vk_link.is_displayed() is True