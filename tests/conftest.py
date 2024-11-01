import pytest
from selenium_helpers import create_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import uuid


@pytest.fixture(scope="function")
def driver():
    driver = create_driver()  # Create a new WebDriver instance
    yield driver               # Provide the driver to the tests
    driver.quit()             # Quit the driver after tests complete


@pytest.fixture(scope="function")
def login(driver):
    # Open the website
    driver.get("https://opensource-demo.orangehrmlive.com")
    # Set an implicit wait
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    # Locate and fill in the username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")
    # Locate and fill in the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    return driver


# General Function
@pytest.fixture(scope="function")
def generate_random_first_name():
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Julia", "Kyle"]
    return random.choice(first_names)

@pytest.fixture(scope="function")
def generate_random_middle_name():
    first_names = ["James", "Marie", "Lee", "Ann", "Ray", "Thomas", "Lynn", "Claire", "Renee", "Joseph", "Jade"]
    return random.choice(first_names)

@pytest.fixture(scope="function")
def generate_random_last_name():
    first_names = ["Johnson", "Brown", "Taylor", "Anderson", "Thompson", "Garcia", "Martinez", "Davis", "Wilson", "Smith", "Ukasah"]
    return random.choice(first_names)

@pytest.fixture(scope="function")
def generate_random_last_name():
    first_names = ["Johnson", "Brown", "Taylor", "Anderson", "Thompson", "Garcia", "Martinez", "Davis", "Wilson", "Smith", "Ukasah"]
    return random.choice(first_names)

@pytest.fixture(scope="function")
def generate_employeeId():
    # Generate a random UUID
    random_uuid = uuid.uuid4()
    # Convert UUID to string and get the first 4 characters
    return str(random_uuid)[:4]

@pytest.fixture(scope="session")
def universalPassword():
    return "temp1234"