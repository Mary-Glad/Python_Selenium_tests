"""
Test QA Studio
"""
from selenium.webdriver.common.by import By

URL = "https://testqastudio.me"

def test_qas(browser):
    """
    Test case - 1 
    """
    browser.get(URL)
    element = browser.find_element(By.CLASS_NAME, "tab-featured")
    element.click()
    table = browser.find_element(By.XPATH, '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a')
    table.click()
    sku = browser.find_element(By.CLASS_NAME, "sku")
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"