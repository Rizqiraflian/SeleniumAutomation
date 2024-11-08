
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element,time,allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

@allure.suite("Manage Employee Tests Suite")
class TestEmployee:
    
    @allure.title(" add new employee")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_add_employee(self,driver,login,generate_random_first_name,generate_random_middle_name,generate_random_last_name,generate_employeeId,globalVariable,capture_screenshot):
        # Use the login fixture to log in
        login(globalVariable["adminUsername"], globalVariable["adminPassword"])

        #--------------
        # access employee menu
        with allure.step("Access PIM menu"):
            employee_menu = driver.find_element(By.XPATH,"//ul/li[2]/a")
            employee_menu.click()

        #--------------
        # click add new employee button
        with allure.step("click add button"):
            add_button = driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
            add_button.click()
            ## assert if the title is displayed
            employee_form_title = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--h6.orangehrm-main-title")
            assert employee_form_title.is_displayed
            time.sleep(3)
            capture_screenshot("create_form_employee")

        #--------------
        # populate data on create employee form
        ## First Name
        with allure.step("input first name value {firstName_value}"):
            input_firstName = driver.find_element(By.NAME, "firstName")
            firstName_value = generate_random_first_name
            input_firstName.send_keys(firstName_value) 
            print(f"first name = {firstName_value}") 
        ## Middle Name
        with allure.step("input middle name value {middleName_value}"):
            input_middleName = driver.find_element(By.NAME, "middleName")
            middleName_value = generate_random_middle_name
            input_middleName.send_keys(middleName_value)
            print(f"middle name = {middleName_value}") 
        ## Last Name
        with allure.step("input last name value {lastName_value}"):
            input_lastName = driver.find_element(By.NAME, "lastName")
            lastName_value = generate_random_last_name
            input_lastName.send_keys(lastName_value) 
            print(f"last name = {lastName_value}")
        ## employee Id
        with allure.step("input employeeId value {employeeId_value}"):
            input_employeeId = driver.find_element(By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
            input_employeeId.send_keys(generate_employeeId) 
            employeeId_value = input_employeeId.get_attribute("value")
            print(f"employeeId = {employeeId_value}")


        #--------------
        #Create Login Details
        with allure.step("click the slider to create login details"):
            slider_createLoginDetails = driver.find_element(By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
            slider_createLoginDetails.click()

        ## set text username
        with allure.step("input username value {username_value}"):
            input_username = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
            username_value = (firstName_value + employeeId_value)
            input_username.send_keys(username_value)
            print(f"username = {username_value}")

        ## check the status radio button is clickable
        with allure.step("test status radio button behavior"):
            btn_statusDisable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
            btn_statusEnable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
            btn_statusDisable.click()
            btn_statusEnable.click()

        ## set text password
        with allure.step("input password value {input_password}"):
            input_password = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
            input_password.send_keys(globalVariable["universalPassword"])
            
        ## set text confirm password
        with allure.step("input password value {input_confirmPassword}"):
            input_confirmPassword = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
            input_confirmPassword.send_keys(globalVariable["universalPassword"])

        #-------------
        # Upload image feature
        ## Locate the input file for upload image
        with allure.step("upload employee image"):
            file_input = driver.find_element(By.CSS_SELECTOR, "input.oxd-file-input") 

            ## Set the file path (relative or absolute)
            relative_file_path = os.path.join("tests", "dataset", "img200x200.jpg")
            absolute_file_path = os.path.abspath(relative_file_path)

            ## Use send_keys() to upload the file
            file_input.send_keys(absolute_file_path)
            capture_screenshot("successfully_populatedEmployeeData")

        #---------
        #click save button
        with allure.step("click save button"):
            submit_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
            submit_btn.click()
            personal_detailPage = wait_for_element(driver, By.XPATH, "(//h6[normalize-space()='Personal Details'])[1]", timeout=10)
            assert personal_detailPage is not None, "redirect failed: personal detail element not found."
            time.sleep(3)
            capture_screenshot("redirect_to_personalDetail")


    
 
    


