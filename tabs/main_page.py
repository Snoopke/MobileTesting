from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class MainWindow:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, what):
        """Checks if element is presented on the screen"""
        try:
            self.driver.find_element_by_id(what)
        except NoSuchElementException:
            return False
        return True

    def should_be_digit_one(self):
        assert self.is_element_present(*MainPageLocators.ONE), 'No button with digit 1'

    def press_digit_one(self):
        button = self.driver.find_element_by_id(*MainPageLocators.ONE)
        button.click()

    def press_digit_two(self):
        button = self.driver.find_element_by_id(*MainPageLocators.TWO)
        button.click()

    def press_digit_three(self):
        button = self.driver.find_element_by_id(*MainPageLocators.THREE)
        button.click()

    def press_digit_four(self):
        button = self.driver.find_element_by_id(*MainPageLocators.FOUR)
        button.click()

    def press_digit_five(self):
        button = self.driver.find_element_by_id(*MainPageLocators.FIVE)
        button.click()

    def press_digit_six(self):
        button = self.driver.find_element_by_id(*MainPageLocators.SIX)
        button.click()

    def press_digit_seven(self):
        button = self.driver.find_element_by_id(*MainPageLocators.SEVEN)
        button.click()

    def press_digit_eight(self):
        button = self.driver.find_element_by_id(*MainPageLocators.EIGHT)
        button.click()

    def press_digit_nine(self):
        button = self.driver.find_element_by_id(*MainPageLocators.NINE)
        button.click()

    def press_digit_zero(self):
        button = self.driver.find_element_by_id(*MainPageLocators.ZERO)
        button.click()

    def press_equals(self):
        button = self.driver.find_element_by_id(*MainPageLocators.EQUALS)
        button.click()

    def press_plus(self):
        button = self.driver.find_element_by_id(*MainPageLocators.PLUS)
        button.click()

    def check_result(self):
        return self.driver.find_element_by_id(*MainPageLocators.RESULTS).text

    def check_formula(self):
        return self.driver.find_element_by_id(*MainPageLocators.FORMULA).text

    def clear_screen(self):
        button = self.driver.find_element_by_id(*MainPageLocators.DELETE)
        button.click()






