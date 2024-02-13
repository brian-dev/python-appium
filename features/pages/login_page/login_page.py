from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:
    def __init__(self, context):
        self.context = context

    def set_login_vals(self, user_type):
        user = self.context.yaml_utils.get_user_info(user_type)
        username_input = self.context.driver.find_element(by=AppiumBy.ID, value='user-name')
        password_input = self.context.browser.find_element(by=AppiumBy.ID, value='password')

        username_input.send_keys(user['username'])
        password_input.send_keys(user['password'])

    def submit_login(self):
        login_btn = self.context.browser.find_element(by=AppiumBy.ID, value='login-button')
        login_btn.click()
