import pytest
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element
from selenium.webdriver.support import expected_conditions as EC
import time



def test_success_add_employee(login,generate_random_first_name,generate_random_middle_name,generate_random_last_name,generate_employeeId,universalPassword):
    driver = login
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    #--------------
    # access employee menu
    employee_menu = driver.find_element(By.XPATH,"//ul/li[2]/a")
    employee_menu.click()
    assert employee_menu is not None, "access failed: Employee menu element not found."

    #--------------
    # click add new employee button
    add_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]")
    add_button.click()
    ## assert if the title is displayed
    employee_form_title = driver.find_element(By.XPATH, "(//h6[normalize-space()='Add Employee'])[1]")
    assert employee_form_title.is_displayed()

    #--------------
    # populate data on create employee form
    ## First Name
    input_firstName = driver.find_element(By.NAME, "firstName")
    firstName_value = generate_random_first_name
    input_firstName.send_keys(firstName_value) 
    print(f"first name = {firstName_value}") 
    ## Middle Name
    input_middleName = driver.find_element(By.NAME, "middleName")
    middleName_value = generate_random_middle_name
    input_middleName.send_keys(middleName_value)
    print(f"middle name = {middleName_value}") 
    ## Last Name
    input_lastName = driver.find_element(By.NAME, "lastName")
    lastName_value = generate_random_last_name
    input_lastName.send_keys(lastName_value) 
    print(f"last name = {lastName_value}")
    ## employee Id
    input_employeeId = driver.find_element(By.CSS_SELECTOR, "div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
    input_employeeId.send_keys(generate_employeeId) 
    employeeId_value = input_employeeId.get_attribute("value")
    print(f"employeeId = {employeeId_value}")

    #--------------
    #Create Login Details
    slider_createLoginDetails = driver.find_element(By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
    slider_createLoginDetails.click()
    ## set text username
    input_username = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    username_value = (firstName_value + employeeId_value)
    input_username.send_keys(username_value)
    print(f"username = {username_value}")
    ## check the status radio button is clickable
    btn_statusDisable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
    btn_statusEnable = driver.find_element(By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]")
    btn_statusDisable.click()
    btn_statusEnable.click()
    ## set text password
    input_password = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
    input_password.send_keys(universalPassword)
    ## set text confirm password
    input_confirmPassword = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
    input_confirmPassword.send_keys(universalPassword)

    #---------
    #click save button
    submit_btn = driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
    submit_btn.click()
    personal_detailPage = wait_for_element(driver, By.XPATH, "(//h6[normalize-space()='Personal Details'])[1]", timeout=10)
    assert personal_detailPage is not None, "redirect failed: personal detail element not found."

    time.sleep(5)

    
 
    


