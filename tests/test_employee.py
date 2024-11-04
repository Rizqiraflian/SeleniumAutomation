
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element,logging,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def test_success_add_employee(login,generate_random_first_name,generate_random_middle_name,generate_random_last_name,generate_employeeId,universalPassword):
    driver = login
    logger = logging.getLogger(__name__)
    
    logger.info("Starting the script...")
    try:
        driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
        #--------------
        # access employee menu
        employee_menu = driver.find_element(By.XPATH,"//ul/li[2]/a")
        employee_menu.click()
        assert employee_menu is not None, "access failed: Employee menu element not found."
        logger.info("successfully access employee menu.")

        #--------------
        # click add new employee button
        add_button = driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        add_button.click()
        ## assert if the title is displayed
        employee_form_title = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--h6.orangehrm-main-title")
        assert employee_form_title.is_displayed()
        logger.info("successfully access create employee form.")

        #--------------
        # populate data on create employee form
        ## First Name
        input_firstName = driver.find_element(By.NAME, "firstName")
        firstName_value = generate_random_first_name
        input_firstName.send_keys(firstName_value) 
        print(f"first name = {firstName_value}") 
        logger.info("first name is insterted.")
        ## Middle Name
        input_middleName = driver.find_element(By.NAME, "middleName")
        middleName_value = generate_random_middle_name
        input_middleName.send_keys(middleName_value)
        print(f"middle name = {middleName_value}") 
        logger.info("middle name is insterted.")
        ## Last Name
        input_lastName = driver.find_element(By.NAME, "lastName")
        lastName_value = generate_random_last_name
        input_lastName.send_keys(lastName_value) 
        print(f"last name = {lastName_value}")
        logger.info("last name is insterted.")
        ## employee Id
        input_employeeId = driver.find_element(By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
        input_employeeId.send_keys(generate_employeeId) 
        employeeId_value = input_employeeId.get_attribute("value")
        print(f"employeeId = {employeeId_value}")
        logger.info("employeeId is insterted.")

        #--------------
        #Create Login Details
        slider_createLoginDetails = driver.find_element(By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
        slider_createLoginDetails.click()
        logger.info("createLoginDetails form is opened.")
        ## set text username
        input_username = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
        username_value = (firstName_value + employeeId_value)
        input_username.send_keys(username_value)
        print(f"username = {username_value}")
        logger.info("username is insterted.")
        ## check the status radio button is clickable
        btn_statusDisable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
        btn_statusEnable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
        btn_statusDisable.click()
        btn_statusEnable.click()
        logger.info("status button is clicked.")
        ## set text password
        input_password = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
        input_password.send_keys(universalPassword)
        logger.info("password is insterted.")
        ## set text confirm password
        input_confirmPassword = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        input_confirmPassword.send_keys(universalPassword)
        logger.info("confirm password is insterted.")

        #-------------
        # Upload image feature
        ## Locate the input file for upload image
        file_input = driver.find_element(By.CSS_SELECTOR, "input.oxd-file-input") 

        ## Set the file path (relative or absolute)
        relative_file_path = os.path.join("tests", "dataset", "img200x200.jpg")
        absolute_file_path = os.path.abspath(relative_file_path)

        ## Use send_keys() to upload the file
        file_input.send_keys(absolute_file_path)

        #---------
        #click save button
        submit_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
        submit_btn.click()
        personal_detailPage = wait_for_element(driver, By.XPATH, "(//h6[normalize-space()='Personal Details'])[1]", timeout=10)
        assert personal_detailPage is not None, "redirect failed: personal detail element not found."
        logger.info("successfully create employee data")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    
 
    


