import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager
from DataDriven import ReadExcel
from selenium.webdriver.common.action_chains import ActionChains


@allure.severity(allure.severity_level.NORMAL)
class TestSample():
    # @pytest.fixture()
    @allure.severity(allure.severity_level.BLOCKER)
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/pct131/PycharmProjects/PytestDemo/chromedriver.exe")
        # driver = webdriver.Chrome(ChromeDriverManager("85.0.4183.83").install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        # yield
        # driver.close()
        # driver.quit()
        # print("Test Completed")

    @allure.severity(allure.severity_level.NORMAL)
    def test_scenario1(self):
        driver.get("https://www.politifact.com/")
        # actions = ActionChains(driver)
        # article2 = driver.find_elements_by_link_text("https://www.politifact.com/factchecks/2021/jan/11/facebook-posts/fact-checking-viral-post-about-impeachment-and-tru/")
        # actions.move_to_element(article2).perform()
        # article1 =
        # test = article2.text
        # print(test)

    def test_scenario3(self):
        amount = driver.find_elements_by_xpath("//*[@class='c-input__field ' and @name='amount']")
        amount.send_keys(15)
        driver.find_elements_by_xpath("//*[@class='c-button' and contains(text(),'Join Now')]").click()
        getamount = driver.find_elements_by_xpath("//*[@id='main']/div/div/div[1]/div/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div/span/input").text
        print(getamount)
        # if getamount == amount:
        #     assert True
        # else:
        #     assert False
























        # if article1== article1header:
        #     assert True
        # else:
        #     assert False



    #     user_name = driver.find_element_by_id("txtUsername")
    #     user_name.send_keys(ReadExcel.Read.username)
    #     pass_word = driver.find_element_by_id("txtPassword")
    #     pass_word.send_keys(ReadExcel.Read.password)
    #     driver.find_element_by_id("btnLogin").click()
    #     title = driver.title
    #     if title=="OrangeHRM1":
    #         assert True
    #     else:
    #         allure.attach(driver.get_screenshot_as_png(), name="TestLogin", attachment_type=AttachmentType.PNG)
    #         assert False
    #
    #



    # @allure.severity(allure.severity_level.MINOR)
    # def test_recruitment(self):
    #     driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()
    #     recruit = driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").is_displayed()
    #     if recruit==True:
    #         assert True
    #     else:
    #         allure.attach(driver.get_screenshot_as_png(), name="TestRecurit", attachment_type=AttachmentType.PNG)
    #         assert False








    @allure.severity(allure.severity_level.CRITICAL)
    def test_teardown(self):
        driver.close()
        driver.quit()
        print("Test Completed")
