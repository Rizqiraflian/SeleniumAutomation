import shutil
import pytest
from selenium_helpers import create_driver,logging,os,allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import uuid

#----------------------------Called Test case -------------------------------

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()  # Create a new WebDriver instance
    driver.implicitly_wait(10)
    yield driver               # Provide the driver to the tests
    driver.quit()             # Quit the driver after tests complete

@pytest.fixture(scope='session', autouse=True)
def clean_allure_results():
    allure_results_dir = './allure-results'
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)
    print(f"Allure results folder cleaned before the test run: {allure_results_dir}")

@pytest.fixture
def capture_screenshot(driver):
    """Fixture to capture a screenshot."""
    def _capture_screenshot(test_name):
        """Capture a screenshot and save it to the specified path."""
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)  # Create the directory if it doesn't exist

        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name=test_name, attachment_type=allure.attachment_type.PNG)

    return _capture_screenshot  # Return the inner function


@pytest.fixture(scope="function")
def login(driver, globalVariable):
    def login_user(username, password):
        driver.get("https://opensource-demo.orangehrmlive.com")
        # Locate and fill in the username
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(globalVariable["adminUsername"])
        # Locate and fill in the password
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(globalVariable["adminPassword"])  
        # Locate and click the login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
    return login_user

#--------------------------------------- General Function---------------------------------------#
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


#-----------------------------------Global Variable------------------------------#

@pytest.fixture(scope="session")
def globalVariable():
    # Define and initialize the global variable(s)
    return {
        "universalPassword": "temp1234",
        "adminUsername": "Admin",
        "adminPassword": "admin123",
        "dummyUsername": "dummyAdmin"
    }