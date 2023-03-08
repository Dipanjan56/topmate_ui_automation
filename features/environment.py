import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities import configReader
from utilities.util_helper import UtilHelper


def before_scenario(context, driver):
    headless_mode = configReader.readConfig("basic info", "headless")
    url = configReader.readConfig("basic info", "test_site_url")

    if configReader.readConfig("basic info", "browser") == "chrome":
        chrome_options = ChromeOptions()
        if headless_mode.lower().strip() == 'true':
            chrome_options.headless = True
        elif headless_mode.lower().strip() == 'false':
            chrome_options.headless = False
        context.driver = webdriver.Chrome(options=chrome_options)

    if configReader.readConfig("basic info", "browser") == "firefox":
        firefox_options = FirefoxOptions()
        if headless_mode.lower().strip() == 'true':
            firefox_options.headless = True
        elif headless_mode.lower().strip() == 'false':
            firefox_options.headless = False
        context.driver = webdriver.Firefox(options=firefox_options)

    context.driver.get(url)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    report_name = 'error_screenshot_' + str(datetime.datetime.now()) + '_' + UtilHelper.get_random_string_with_uuid()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name=report_name,
                      attachment_type=allure.attachment_type.PNG)
