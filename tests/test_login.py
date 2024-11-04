import pytest
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element,allure,os


@allure.suite("Login Tests Suite")
class TestLogin:
    
    @allure.title("Successful Login Test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success(self, driver,adminUsername,adminPassword,capture_screenshot):
        with allure.step("Access orangeHRMDemo website"):
            driver.get("https://opensource-demo.orangehrmlive.com")
            # Set an implicit wait
            driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
        with allure.step("Input admin username {adminUsername} with password {adminPassword}"):
            # Locate and fill in the username
            username_field = driver.find_element(By.NAME, "username")
            username_field.send_keys(adminUsername)
            # Locate and fill in the password
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(adminPassword)
        with allure.step("click login button"):    
            # Locate and click the login button
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
        with allure.step("Verify dashboard element is exist"):
            # Use the wait function from selenium_helpers to verify login success
            dashboard_element = wait_for_element(driver, By.XPATH, "//div[@id='app']//div//div//header//div//div//span//h6", timeout=10)
            try:
                assert dashboard_element.is_displayed, "Dashboard Element is not visible"
                capture_screenshot("login_success")
            except AssertionError:
                capture_screenshot("login_failed")
                raise

    @allure.title("Failed Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_failed(self, driver,admin_wrongUsername,universalPassword,capture_screenshot):
        with allure.step("Access orangeHRMDemo website"):
            driver.get("https://opensource-demo.orangehrmlive.com")
            # Set an implicit wait
            driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
        with allure.step("Input admin username {admin_wrongUsername} with password {universalPassword}"):
            # Locate and fill in the username
            username_field = driver.find_element(By.NAME, "username")
            username_field.send_keys(admin_wrongUsername)
            # Locate and fill in the password
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(universalPassword)
        with allure.step("click login button"):
            # Locate and click the login button
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
        with allure.step("Verify the error validation"):
            error_validation = wait_for_element(driver, By.XPATH, "//div[@role='alert']//div[1]", timeout=10)
            try:
                assert error_validation.is_displayed
                capture_screenshot("error message is displayed")
            except AssertionError:
                capture_screenshot("error message is not displayed")
                raise 


