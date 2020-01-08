def go_to_login_page(driver):
    login_link = driver.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    driver.get(link)
    go_to_login_page(driver)