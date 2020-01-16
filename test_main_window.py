from .tabs.main_page import MainWindow
from .tabs.locators import MainWindowLocators


def test_should_be_digit_one(driver):
    window = MainWindow(driver)
    window.should_be_button_one()


def test_input_digit_one(driver):
    window = MainWindow(driver)
    window.input_digit_one()


def test_is_digit_one_presents(driver):
    window = MainWindow(driver)
    window.is_element_present(MainWindowLocators.NINE)
