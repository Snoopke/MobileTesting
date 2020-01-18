import pytest

from .tabs.main_page import MainWindow


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


def test_subtraction(driver):
    """ 70 - 89 = -19"""
    step = MainWindow(driver)
    step.press_digit_seven()
    step.press_digit_zero()
    step.press_minus()
    step.press_digit_eight()
    step.press_digit_nine()
    result = step.check_result()
    assert result == '-19', 'Expected {}. Actual result {}'.format('-19', result)


def test_multiplication(driver):
    """ 26 * 2 = 52 """
    step = MainWindow(driver)
    step.press_digit_two()
    step.press_digit_six()
    step.press_times()
    step.press_digit_two()
    result = step.check_result()
    assert result == '52', 'Expected {}. Actual result {}'.format('52', result)


def test_division(driver):
    """ 62 / 4 = 15,5"""
    step = MainWindow(driver)
    step.press_digit_six()
    step.press_digit_two()
    step.press_divide()
    step.press_digit_four()
    result = step.check_result()
    assert result == '15,5', 'Expected {}. Actual result {}'.format('15,5', result)


@pytest.mark.xfail
def test_combination(driver):
    """ 1 + 5 * 4 - 3 / 7 = 3"""
    step = MainWindow(driver)
    step.press_digit_one()
    step.press_plus()
    step.press_digit_five()
    step.press_times()
    step.press_digit_four()
    step.press_minus()
    step.press_digit_three()
    step.press_divide()
    step.press_digit_seven()
    step.press_equals()
    result = step.check_result()
    assert result == '3', 'Expected {}. Actual result {}'.format('3', result)


def test_leading_zeros_test(driver):
    """Try input 000"""
    step = MainWindow(driver)
    step.press_digit_zero()
    step.press_digit_zero()
    step.press_digit_zero()
    result = step.check_formula()
    assert result == '0', 'Expected {}. Actual result {}'.format('0', result)
