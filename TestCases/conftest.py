import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser_invoke(request):     #here request is fixture instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


