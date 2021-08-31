#! /usr/bin/python

import pytest
from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Data import Data
from utilities.HelperFunction import *


class Test_ValidateFilterDropdown(Base):

    def test_FilterHeaderText(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)

        actualSortingText = actions.getText(hp.getSortingText())
        log.info("Filter header text: {}".format(actualSortingText))
        expectedSortingText = getData["FilterText"]

        assert actualSortingText == expectedSortingText

    def test_validateTableHeader(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        expectedTableHeader = ['NAME', 'NUMBER OF CASES', 'AVERAGE IMPACT SCORE', 'COMPLEXITY']
        actualTableHeader = actions.getTableHeader(hp.getTableHeader())
        if actualTableHeader == expectedTableHeader:
            log.info("TableHeader found as expected: {}".format(actualTableHeader))
        else:
            log.info("MissMatch found in TableHeader..")
            log.debug("actualTableHeader: {} , expectedTableHeader: {}".format(actualTableHeader, expectedTableHeader))
            assert actualTableHeader == expectedTableHeader

    def test_DropdownEnabled(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        actions.selectDropDownList(hp.selectDropDownsElement())
        actualDropdownClickable = actions.selectedDropDown(hp.selectDropDownsElement())
        log.info("Dropdown enable {}".format(actualDropdownClickable))
        expectedDropdownClickable = getData["DropDown"]
        assert actualDropdownClickable == expectedDropdownClickable

    def test_validateDropdown(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        expectedSortingText = ['Name', 'Number of cases', 'Impact score', 'Complexity']
        actualSortingText = actions.selectAllDropDown(hp.getValidDropDown())
        log.info("Dropdown list: {}".format(actualSortingText))
        assert actualSortingText == expectedSortingText

    def test_selectColumnName(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        selectColumnHeader = str(getData["SelectColumnForSorting"])
        element = hp.selectDropDownsElement()
        log.info("Select column for apply to sorting!")
        actions.columnSelectToSort(selectColumnHeader, element)

    def test_columnCheck(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        # Select the desired column header to sort the table
        actualTableHeader = actions.getTableHeader(hp.getTableHeader())
        # Select the desired column header to sort the table
        selectColumnHeader = getData["SelectColumnForSorting"]
        if validate_element(selectColumnHeader, actualTableHeader):
            log.info("Element found.")
        else:
            assert self.validate_element(getData) == True

    @pytest.fixture(params=Data.getTestData("TC2"))
    def getData(self, request):
        return request.param
