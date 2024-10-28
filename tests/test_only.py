import pytest
from selenium.webdriver.common.by import By
from .conftest import browser


def test_check_footer(browser):
    browser.get('https://only.digital/')
    footer = browser.find_element(By.XPATH, "//footer")
    assert footer


@pytest.mark.parametrize("url", [
    'https://only.digital/', 'https://only.digital/projects', 'https://only.digital/company', 'https://only.digital/job'

])
def test_check_elements_social_in_footer(browser, url):
    browser.get(url)
    awwwards = browser.find_element(By.XPATH, "(//a[@href='https://www.awwwards.com/Ilyaredko/'])[2]").get_attribute('href')
    vk = browser.find_element(By.XPATH, "(//a[@href='https://vk.com/onlydigitalagency'])[2]").get_attribute('href')
    telegram = browser.find_element(By.XPATH, "(//a[@href='https://t.me/onlycreativedigitalagency'])[2]").get_attribute('href')
    vimeo = browser.find_element(By.XPATH, "(//a[@href='https://vimeo.com/onlydigital'])[2]").get_attribute('href')
    behance = browser.find_element(By.XPATH, "(//a[@href='https://www.behance.net/onlydigitalagency'])[2]").get_attribute('href')
    assert awwwards == 'https://www.awwwards.com/Ilyaredko/'
    assert vk == 'https://vk.com/onlydigitalagency'
    assert telegram == 'https://t.me/onlycreativedigitalagency'
    assert vimeo == 'https://vimeo.com/onlydigital'
    assert behance == 'https://www.behance.net/onlydigitalagency'



