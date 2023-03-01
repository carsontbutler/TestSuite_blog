from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# def test_go_to_register_page_via_url(driver, wait):
#     register_page_url = f'{url}/register/'
#     register_page_locator = '/html/body/main/div/div[1]/div/form/fieldset/legend'
#     expected_result = 'Join Today'
    
#     driver.get(register_page_url)
#     locator = wait.until(EC.presence_of_element_located((By.XPATH, register_page_locator))).text
#     assert locator == expected_result
    