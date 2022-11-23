from selene.support.shared import browser
import pytest

link = 'https://google.com'


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(link)
