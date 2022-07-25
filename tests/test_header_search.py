# -*- encoding=utf8 -*-
from tests.conftests import web_driver_desktop

import pytest

from pages.aux_methods import AuxMetods
from pages.pages import Headers
from pages.locators import StartLocators


# 1
def test_search_opens_page(web_driver_desktop):
    """Тест проверяет, что открывается страница с корректными результатами поиска"""
    page = Headers(web_driver_desktop)
    page.search_field_click("book")

    assert "book" in page.driver.current_url


# 2
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("test_search", ['фентези', 'приключения', 'Harry Potter', 'Приключения Оливера твиста',
                                         'в мире животных', 2000]
    , ids=['ru', 'more_ru', 'eng', 'more_eng', 'more_eng_ru', 'digit'])
def test_search_positive(web_driver_desktop, test_search):
    """Тест проверяет работу поиска с различными позитивными данными, делает скриншот"""

    page = Headers(web_driver_desktop)
    page.search_field_click(test_search)
    page.save_screen_browser(f'test_search_{test_search}')
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text[0])

    assert amount > 0, 'Field "Search" working unsucсess'


# 3

@pytest.mark.negative
@pytest.mark.parametrize("test_search",
                         [AuxMetods.generate_string(255), AuxMetods.generate_string(1001)
                             , AuxMetods.russian_chars(), AuxMetods.russian_chars().upper(), AuxMetods.english_chars()
                             , AuxMetods.special_chars()],
                           ids=['255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'english', 'specials'])
def test_search_negative(web_driver_desktop, test_search):
    """Тест проверяет поле поиска с различными негативными данными и корректность обработки запроса"""

    page = Headers(web_driver_desktop)
    page.search_field_click(test_search)
    text = web_driver_desktop.find_element(*StartLocators.search_error).text
    # Заметка удалить, посмотреть в прошлой работе как сделать якорь правильно

    assert text == 'Мы ничего не нашли по вашему запросу! Что делать?', 'Field "Search" working unsucсess'


# 4
def test_books_have_image(web_driver_desktop):
    """Тест проверяет, что у всех найденных книг на странице есть фото """
    page = Headers(web_driver_desktop)
    page.search_field_click("Джоан Роулинг")

    quantity_of_book_on_the_page = len(page.driver.find_elements(*StartLocators.found_books))
    images = page.driver.find_elements(*StartLocators.book_images)
    assert len(images) == quantity_of_book_on_the_page


# 5
def test_sort_by_low_price(web_driver_desktop):
    """Тест проверяет, что сортировка "сначала дешевые" работает корректно"""
    page = Headers(web_driver_desktop)
    page.search_field_click("Путешествия Гулливера")

    page.driver.find_element(*StartLocators.sort_by_btn).click()
    page.driver.find_element(*StartLocators.sort_by_low_price).click()
    page.wait_page_loaded()
    prices = page.driver.find_elements(*StartLocators.books_prices)
    all_prices = []
    for price in prices:
        all_prices.append(float(price.text.replace(' ', '')))
    assert all_prices == sorted(all_prices)


# 6
def test_sort_by_high_price(web_driver_desktop):
    """Тест проверяет, что сортировка "сначала дорогие" работает корректно"""
    page = Headers(web_driver_desktop)
    page.search_field_click("Великий Гетсби")

    page.driver.find_element(*StartLocators.sort_by_btn).click()
    page.driver.find_element(*StartLocators.sort_by_high_price).click()
    page.wait_page_loaded()
    prices = page.driver.find_elements(*StartLocators.books_prices)
    all_prices = []
    for price in prices:
        all_prices.append(float(price.text.replace(' ', '')))
    assert all_prices == sorted(all_prices, reverse=True)


# 7
def test_add_to_cart(web_driver_desktop):
    """Тест проверяет добавление книги в корзину"""
    page = Headers(web_driver_desktop)
    page.search_field_click("Сталин")
    page.driver.find_elements(*StartLocators.add_to_cart_buttons)[1].click()  # first book - click "to cart"
    page.wait_page_loaded()
    assert "1" in page.driver.find_element(*StartLocators.amount_in_cart).text
