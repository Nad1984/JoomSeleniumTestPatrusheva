from selenium.webdriver import Chrome
import pytest as pytest
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def joom_browser():
    chrome_browser = Chrome(executable_path=ChromeDriverManager().install())
    chrome_browser.maximize_window()
    chrome_browser.get("https://www.joom.com/en")

    yield chrome_browser

    chrome_browser.quit()

    # chrome_options = webdriver.ChromeOptions()
    # prefs = {"profile.default_content_setting_values.notifications": 2}
    # chrome_options.add_experimental_option("prefs", prefs)
    # driver = webdriver.Chrome(chrome_options=chrome_options)


@pytest.fixture
def chrome_joom_browser():
    # Creating Instance
    option = Options()

    # Working with the 'add_argument' Method to modify Driver Default Notification
    option.add_argument('--disable-notifications')

    # Passing Driver path alongside with Driver modified Options
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=option)

    # Do your stuff and quit your driver/ browser
    browser.maximize_window()
    browser.get('https://www.joom.com/en')

    yield browser
    browser.quit()
