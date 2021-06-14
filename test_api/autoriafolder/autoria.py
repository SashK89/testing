from selenium import webdriver
import time
class AutoRiaMainPage:
    def __init__(self):
        self.driver = webdriver.Chrome(r"D:\python_books\.env\test_api\webdriver\chromedriver.exe")
        self.driver.get("https://auto.ria.com/uk/")
        self.driver.maximize_window()

    def search_items_moto(self):
        search_field_auto = self.driver.find_element_by_class_name("elem-tab").click()
        time.sleep(3)
        search_field_auto = self.driver.find_element_by_xpath("/html/body/div[6]/section[1]/div[1]/div/div/form/div[1]/div[1]/div[1]/div/select").click()
        time.sleep(3)
        search_field_auto = self.driver.find_element_by_xpath("/html/body/div[6]/section[1]/div[1]/div/div/form/div[1]/div[1]/div[1]/div/select/option[3]").click()
        time.sleep(3)
        search_field_auto = self.driver.find_element_by_class_name("button-primary").click()
        time.sleep(5)
        
    def show_items(self):
        return len(self.driver.find_elements_by_css_selector("#searchResults > section:nth-child(9) > div.content-bar > div.ticket-photo.loaded > a > picture > img"))



    