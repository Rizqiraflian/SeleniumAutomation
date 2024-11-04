import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Function to set up the WebDriver
def create_driver():
    logging.basicConfig(level=logging.INFO)
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Helper function for wait until an element is visible
def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

# Other reusable functions can be added here
