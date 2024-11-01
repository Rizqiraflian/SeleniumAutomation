import pytest
from selenium.webdriver.common.by import By
from selenium_helpers import wait_for_element
import time



def test_success_add_employee(login,generate_random_first_name,generate_random_middle_name,generate_random_last_name,generate_employeeId):
    driver = login
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    # access employee menu
    employee_menu = driver.find_element(By.XPATH,"//ul/li[2]/a")
    employee_menu.click()
    assert employee_menu is not None, "access failed: Employee menu element not found."

    # click add new employee button
    add_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]")
    add_button.click()
    # assert if the title is displayed
    employee_form_title = driver.find_element(By.XPATH, "(//h6[normalize-space()='Add Employee'])[1]")
    assert employee_form_title.is_displayed()
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
    time.sleep(5)

    
 
    


