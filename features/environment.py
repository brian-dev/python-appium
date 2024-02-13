from appium.webdriver.appium_service import AppiumService
from behave import fixture, use_fixture
from dotenv import load_dotenv
from features.pages.login_page.login_page import LoginPage
from features.pages.products_page.products_page import ProductsPage
from features.utils.driver import Driver
# from features.utils.browser_methods import BrowserMethods
from features.utils.yaml_utils import YamlUtils


@fixture
def config_appium_server(context):
    service = AppiumService()
    yield service.start()
    service.stop()


@fixture
def load_helper_classes(context):
    # context.browser_methods = BrowserMethods(context)
    context.yaml_utils = YamlUtils()


@fixture
def config_driver(context):
    load_dotenv()
    context.android = Driver.android_driver(context)
    yield context.android
    context.android.quit()


@fixture
def load_page_classes(context):
    context.login_page = LoginPage(context)
    context.products_page = ProductsPage(context)


def before_all(context):
    use_fixture(config_appium_server, context)
    use_fixture(config_driver, context)
    use_fixture(load_helper_classes, context)
    use_fixture(load_page_classes, context)
