import pytest
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element

def test_login_success(driver):
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
    # Use the wait function from selenium_helpers to verify login success
    dashboard_element = wait_for_element(driver, By.XPATH, "//div[@id='app']//div//div//header//div//div//span//h6", timeout=10)
    assert dashboard_element is not None, "Login failed: Dashboard element not found."

def test_login_failed(driver):
    # Open the website
    driver.get("https://opensource-demo.orangehrmlive.com")
    # Set an implicit wait
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    # Locate and fill in the username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin2")
    # Locate and fill in the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin1233")
    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    # Use the wait function from selenium_helpers to verify login success
    error_validation = wait_for_element(driver, By.XPATH, "//div[@role='alert']//div[1]", timeout=10)
    assert error_validation is not None, "Login is success. error validation is not appear"

