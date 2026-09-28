from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Microsoft Edge Driver
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Verify page title
assert driver.title.strip() != ""
print(f"Page title test passed: '{driver.title}'")

# Enter name field branded with arkarup
name_field = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)

name_field.clear()
name_field.send_keys("arkarup")

assert name_field.get_attribute("value") == "arkarup"
print("Name field test passed for arkarup")

# Select Radio2
radio2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='radio2']")
    )
)

radio2.click()

assert radio2.is_selected()
print("Radio2 test passed")

# Trigger Alert
alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='Alert']")
    )
)

alert_button.click()

# Verify alert text contains arkarup
alert = wait.until(
    EC.alert_is_present()
)

print("Alert text:", alert.text)

assert alert is not None
assert "arkarup" in alert.text

alert.accept()

print("Alert test passed")
print("All Selenium tests passed successfully by arkarup")

driver.quit()
