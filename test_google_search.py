from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene(open_browser):
    assert browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in '
                                                             'Python'))


def test_google_should_not_find_freaky_text(open_browser):
    freaky_text = 'zxcffddghhhh'
    assert browser.element('[name="q"]').should(be.blank).type(freaky_text).press_enter()
    assert browser.element('[id="res"]').should(have.text(f'По запросу {freaky_text} ничего не найдено.'))





