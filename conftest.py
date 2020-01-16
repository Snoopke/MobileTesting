import pytest
from appium import webdriver


DESIRED_CAPS = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'c45de6f2',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.dalviksoft.calculator',
    'appActivity': 'com.android2.calculator3.Calculator'
}


@pytest.fixture(scope='function')
def driver():
    print('starting app...')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)
    driver.implicitly_wait(15)
    yield driver
    print('quiting app...')
    driver.quit()