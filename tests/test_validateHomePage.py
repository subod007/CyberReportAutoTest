#! /usr/bin/python
import pytest
from actions.Actions import Actions
from utilities.Base import Base
from utilities.Data import Data
from pageObjects.HomePage import HomePage

class Test_ValidateSorting(Base):


    def test_validateClearFlterTextBox(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        actualTextBoxStatus=actions.getText(hp.getFilterText())
        expectedTextBoxStatus = getData["FilterText"]
        actualFiltertext = actions.getText(hp.getFilterText())

        assert actualFiltertext == expectedTextBoxStatus

        if actualTextBoxStatus == expectedTextBoxStatus:
            log.info("Textbox is alrady cleared.")
        else:
            actualTextBoxStatus = actions.clear((hp.getFilterText()))
            log.info("Textbox cleared successfully.")

        assert actualTextBoxStatus == expectedTextBoxStatus


    def test_validatePageText(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)

        actualText = actions.getText(hp.getText())
        log.info("Page text: {}".format(actualText))
        expectedText = getData["Text"]

        assert actualText == expectedText


    def test_validateHomeTitle(self, getData):
        log = self.getLogger()
        actions = Actions(self.driver)

        actualTitle = actions.getTitle()
        log.info("Page title: {}".format(actualTitle))
        expectedTitle = str(getData["Title"])
        assert actualTitle == expectedTitle

    @pytest.fixture(params=Data.getTestData("TC1"))
    def getData(self, request):
        return request.param