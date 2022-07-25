import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def web_driver_desktop():
    web_driver = webdriver.Chrome("/Users/bato/Desktop/chrome/chromedriver")
    web_driver.maximize_window()
    web_driver.implicitly_wait(5)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_var_size(width: int):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные значения User-Agent, загружает веб-драйвер Хром,
    принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные), после выполнения основного кода
    закрывает браузер"""

    option = webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path='/Users/bato/Desktop/chrome/chromedriver', options=option)
    web_driver.set_window_size(width, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()





