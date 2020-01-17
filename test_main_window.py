from .tabs.main_page import MainWindow
import pytest


@pytest.mark.skip
def test_should_be_digit_one(driver):
    """Example of test which checks if element is presented on screen"""
    step = MainWindow(driver)
    step.should_be_digit_one()


@pytest.mark.skip
def test_press_digit_one(driver):
    step = MainWindow(driver)
    step.press_digit_one()
    result = step.check_formula()
    assert result == '1', 'Expected 1 on screen'


def test_input_all_digits(driver):
    """Input 1234567890"""
    step = MainWindow(driver)
    step.press_digit_one()
    step.press_digit_two()
    step.press_digit_three()
    step.press_digit_four()
    step.press_digit_five()
    step.press_digit_six()
    step.press_digit_seven()
    step.press_digit_eight()
    step.press_digit_nine()
    step.press_digit_zero()
    result = step.check_formula()
    assert result == '1 234 567 890', 'Expected {}. Actual result: {}'.format('1 234 567 890', result)


def test_sum_of_two_integers(driver):
    """1 + 4 = 5"""
    step = MainWindow(driver)
    step.press_digit_one()
    step.press_plus()
    step.press_digit_four()
    result = step.check_result()
    assert result == '5', 'Expected {}. Actual result {}'.format('5', result)


def test_delete_last_digit(driver):
    step = MainWindow(driver)
    step.press_digit_two()
    step.press_digit_nine()
    step.delete_last_digit()
    result = step.check_formula()
    assert result == '2', 'Expected {}. Actual result {}'.format('2', result)


def test_clear_the_screen(driver):
    step = MainWindow(driver)
    step.press_digit_eight()
    step.press_digit_zero()
    step.press_digit_seven()
    step.clear_the_screen()
    result = step.check_formula()
    assert result == '', 'Expected {}. Actual result {}'.format('', result)
