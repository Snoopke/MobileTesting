from appium.common.exceptions import NoSuchContextException
from .locators import MainWindowLocators


class MainWindow:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, what):
        """Метод ищет элемент на странице"""
        try:
            self.driver.find_element_by_id(what)
        except NoSuchContextException:
            return False
        return True

    def should_be_button_one(self):
        assert self.is_element_present(MainWindowLocators.ONE), 'No button with digit 1'






