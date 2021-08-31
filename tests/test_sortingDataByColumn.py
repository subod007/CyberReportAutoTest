#! /usr/bin/python
import pytest
from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Data import Data
from utilities.HelperFunction import *


class Test_Validate_TableSorting(Base):

    def test_VelidateSortedData(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)
        # Get Filter Flag from input data file!
        checkFilterFlag = getData["ApplyFilterFlag"]
        if checkFilterFlag:
            # Enter text into the filter data text box
            selectColumnHeader = str(getData["InputText"])
            log.info("selectColumnHeader : {}".format(selectColumnHeader))
            actions.sendKeys(hp.getFilterTextBox(), selectColumnHeader)
            Actions.enterTextInFilterBox(selectColumnHeader, hp.getFilterTextBox())
            webTableBeforeSort = actions.getTableData((hp.getTableData()))
            log.info("Default webTable data with filter: {}".format(webTableBeforeSort))
            assert checkWebListLength(
                webTableBeforeSort) == 1, "No data /Only one row found for the for given filter in " \
                                          "input data file! "
        else:
            webTableBeforeSort = actions.getTableData((hp.getTableData()))
            log.info("Default webTable data without filter: {}".format(webTableBeforeSort))
            assert checkWebListLength(
                webTableBeforeSort) == 1, "No data /Only one row found for the for given filter in " \
                                          "input data file! "

        # Select value from dropdown to sort the WebTable
        selectColumn = str(getData["SelectColumnForSorting"])
        log.info("selectColumn: {}".format(selectColumn))
        element = hp.selectDropDownsElement()
        actions.columnSelectToSort(selectColumn, element)

        # Get all the Table header in list
        listOfTableHeader = actions.getTableHeader(hp.getTableHeader())
        log.info("WebTable headers: {}".format(listOfTableHeader))

        # Get the index value of the column selected from dropdown
        getSortedColumnIndex = getIndexColumn(listOfTableHeader, selectColumn)
        log.info("get Sorted Column Index: {}".format(getSortedColumnIndex))

        # Sorted the default data without dropdown selection
        defaultDataSorted = selectSortingMethod(selectColumn, webTableBeforeSort, getSortedColumnIndex)
        log.info("get default data after sort for give column: {}".format(defaultDataSorted))

        # Sorted the Table data after apply the selection from dropdown
        webDataAfterSelectSort = actions.getTableData((hp.getTableData()))
        log.info("WebTable Data after apply the selection from dropdown : {}".format(webDataAfterSelectSort))

        if checkSortByHeader(selectColumn):
            log.info(checkSortByHeader(selectColumn))
            webDataAfterFormate = frameData(webDataAfterSelectSort, getSortedColumnIndex)
            log.info("WebTable Data After the Formatting for NUMBER OF CASES: {}".format(webDataAfterFormate))
            assert webDataAfterSelectSort == webDataAfterFormate, "Data mismatch found!"
        else:
            assert webDataAfterSelectSort == defaultDataSorted, "Data mismatch found!"

    @pytest.fixture(params=Data.getTestData("TC3"))
    def getData(self, request):
        return request.param
