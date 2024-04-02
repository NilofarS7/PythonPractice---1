import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass


class TestFormSubmission(BaseClass):

    def test_WebformSubmission(self, MultipleDataLoad):
        self.driver.find_element(By.XPATH, "//input[@name = 'name'][1]").send_keys(MultipleDataLoad["Name"])
        self.driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys(MultipleDataLoad["Email"])
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(MultipleDataLoad["Password"])
        self.driver.find_element(By.ID, "exampleCheck1").click()
        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)
        self.driver.find_element(By.XPATH, "//input[@value = 'option2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name = 'bday']").send_keys(MultipleDataLoad["birth"])
        self.driver.find_element(By.CSS_SELECTOR, "input[value = 'Submit']").click()
        final_message = self.driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
        print(final_message)
        assert "Success" in final_message
        self.driver.find_element(By.XPATH, "//input[@class = 'ng-untouched ng-pristine ng-valid']").clear()
        self.driver.refresh()
        time.sleep(3)

    #This is List of Tuple
    #@pytest.fixture(params=[("Nilofar Shaikh", "abc@xyz.com", "Test1", "07-04-1991"), #can be used as send_keys(MultipleDataLoad[0]) above
                           # ("Nilo", "mno@xyz.com", "test2", '15-11-1995'),
                           # ("Safari", "abc@mno.com", "test3", "05-03-1964"),
                           # ("Edge", "test@xyz.com", "testing", "08-08-2000")])

    #This is List of Dictionary
    @pytest.fixture(params=[{"Name": "Nilofar Shaikh", "Email": "abc@xyz.com", "Password": "Test1", "birth": "07-04-1991"},
                            {"Name": "Nilo", "Email": "mno@xyz.com", "Password": "Test2", "birth": "08-08-2000"}])
    def MultipleDataLoad(self, request):
        return request.param



