import pytest
from selenium_helpers import create_driver

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()  # Create a new WebDriver instance
    yield driver               # Provide the driver to the tests
    driver.quit()             # Quit the driver after tests complete
