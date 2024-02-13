import os

from appium import webdriver


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    platformVersion='13.0',
    browserName='Chrome',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class Driver:
    def __init__(self):
        pass

    def android_driver(self):
        driver = webdriver.Remote(appium_server_url, capabilities)
        return driver
