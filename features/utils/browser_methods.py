# import time
#
# from selenium.webdriver.common.by import By
#
#
# class BrowserMethods:
#     def __init__(self, context):
#         self.context = context
#
#     def sleep(self, num_secs):
#         time.sleep(num_secs)
#
#     def goto(self, url):
#         self.context.browser.get(url)
#
#     def click(self, element):
#         element.click()
#
#     def get_element_by_id(self, value):
#         return self.driver.find_element(By.ID)
#
#     def get_current_url(self):
#         return self.context.browser.current_url
#
#     def validate_url(self, page):
#         current_url = self.get_current_url()
#         url_file = self.context.yaml_utils.get_env_urls()
#         expected_url = url_file['base_url'] + url_file[page]
#         return current_url, expected_url
