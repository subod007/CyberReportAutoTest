#! /usr/bin/python
import re
import pytest
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from utilities.Base import Base

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, es, fr, ru, it, pt etc.")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path=Base.ROOT_PATH + "/resources/chromedriver.exe", options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=Base.ROOT_PATH + "/resources/geckodriver")
    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path=Base.ROOT_PATH + "/resources/IEDriverServer.exe")
        print("Browser value passed from command line: " + browser_name)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    driver.get("https://mystifying-beaver-ee03b5.netlify.app/")  # get the url from conf file

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            tc_name = re.sub(r"\[.*\]", '', tc_name)
            file_name = Base.ROOT_PATH + "/reports/screenshots/" + tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
