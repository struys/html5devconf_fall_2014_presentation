import getpass

import testify as T
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from examples.utils import with_driver


class TestYelpSearch(T.TestCase):

    @with_driver(
        DesiredCapabilities.FIREFOX,
        DesiredCapabilities.CHROME,
        DesiredCapabilities.SAFARI,
    )
    def test_simple_interactions(self, driver):
        driver.get("http://yelp.com")
        driver.find_element_by_css_selector('#find_desc').send_keys('Pizza')
        driver.find_element_by_css_selector('#header-search-submit').click()

        driver.find_element_by_css_selector('input[value="CA:San_Francisco::SoMa"]').click()

        driver.find_element_by_css_selector('a[href="/biz/zero-zero-san-francisco"]')

        driver.find_element_by_css_selector('.mo-map-trigger').click()

