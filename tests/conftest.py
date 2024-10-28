from selenium import webdriver
from chromedriver_py import binary_path
import pytest
from logger import setup_logger

logger = setup_logger()


@pytest.fixture(scope="session")
def browser():
    logger.info("Start")
    svc = webdriver.ChromeService(executable_path=binary_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=svc, options=options)
    options.headless = True
    driver.implicitly_wait(10)
    logger.info("stop")
    yield driver
    driver.quit()