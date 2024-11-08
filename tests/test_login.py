from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element,allure,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.suite("Login Tests Suite")
class TestLogin:
    
    @allure.title("Successful Login Test")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success(self, driver,capture_screenshot,globalVariable):
        with allure.step("Access orangeHRMDemo website"):
            driver.get("https://opensource-demo.orangehrmlive.com")
        with allure.step("Input admin username {adminUsername} with password {adminPassword}"):
            # Locate and fill in the username
            username_field = driver.find_element(By.NAME, "username")
            username_field.send_keys(globalVariable["adminUsername"])
            # Locate and fill in the password
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(globalVariable["adminPassword"])
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

    @allure.title("Test Error Validation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_failed(self,driver,globalVariable,capture_screenshot):
        with allure.step("Access orangeHRMDemo website"):
            driver.get("https://opensource-demo.orangehrmlive.com")
        
        # Check the validation if the credential is invalid
        with allure.step("Check if the credential is invalid"):
            with allure.step("input invalid username"):
                # Locate and fill in the username
                username_field = driver.find_element(By.NAME, "username")
                username_field.send_keys(globalVariable["dummyUsername"])
            with allure.step("input invalid password"):
                # Locate and fill in the password
                password_field = driver.find_element(By.NAME, "password")
                password_field.send_keys(globalVariable["adminPassword"])
        with allure.step("click login button"):
            # Locate and click the login button
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
        with allure.step("Verify the error handling for invalid credential is correct"):
            error_validation = wait_for_element(driver, By.XPATH, "//div[@role='alert']//div[1]", timeout=10)
            try:
                assert error_validation.is_displayed
                capture_screenshot("error message is displayed")
            except AssertionError:
                capture_screenshot("error message is not displayed")
                raise 

        # Check the validation if the mandatory field is not populated
        username_field = driver.find_element(By.NAME, "username")
        username_field.clear()
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        with allure.step("Check the mandatory field validation"):
            with allure.step("click login button with blank value of username and password"):
                # Locate and click the login button
                login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                login_button.click()
            with allure.step("Verify the error handling for mandatory field"):
                error_validation_username = wait_for_element(driver, By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[1]", timeout=10)
                error_validation_password = wait_for_element(driver, By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[2]", timeout=10)
                try:
                    assert error_validation_username.is_displayed
                    assert error_validation_password.is_displayed
                    capture_screenshot("error message is displayed")
                except AssertionError:
                    capture_screenshot("error message is not displayed")
                    raise 