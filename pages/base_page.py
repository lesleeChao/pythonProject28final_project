from time import sleep
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """ Конструктор класса - метод init, получающий объект веб-драйвера, адрес страницы и время ожидания элемента"""

    def __init__(self, driver, url, wait=3):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(wait)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def save_screen_browser(self, name: str):
        self.driver.save_screenshot(f'screenshots\\{name}.png')

    def goto_page(self, num: int) -> str:
        if num == 1:
            goto_url = self.url
        else:
            goto_url = f'{self.url}?page={num}'
        return goto_url

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:
            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self.driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self.driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self.driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def save_screen_browser_2(self, name: str):
        self.driver.save_screenshot(f'screenshots\\{name}.png')

    def win_scroll_begin(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def win_scroll(self, scroll_point=3500):
        self.driver.execute_script(f"window.scrollTo(0, {scroll_point})")