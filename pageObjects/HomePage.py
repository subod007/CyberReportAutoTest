#! /usr/bin/python

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    filterTextBox = (By.ID, "filter-input")
    filterText = (By.XPATH, "//label[contains(text(),'Filter data')]")
    sortingText = (By.XPATH, "//label[contains(text(),'Sort data')]")
    homePageTitle = (By.CSS_SELECTOR, "h1")
    dropDownsName = (By.XPATH, "//select[@name='sort-select']/option")
    dropDownsElement = (By.XPATH, "//select[@name='sort-select']")
    tableHeader = (By.XPATH, "//*[@class='table-header']")
    tableData = (By.XPATH, "//*[@class='table-row']")

    def selectDropDownsElement(self):
        return self.driver.find_element(*HomePage.dropDownsElement)

    def getFilterText(self):
        return self.driver.find_element(*HomePage.filterText)

    def getText(self):
        return self.driver.find_element(*HomePage.homePageTitle)

    def selectedDropDown(self):
        return self.driver.find_element(*HomePage.dropDownsElement)

    def getFilterTextBox(self):
        return self.driver.find_element(*HomePage.filterTextBox)

    def getSortingText(self):
        return self.driver.find_element(*HomePage.sortingText)

    def getValidDropDown(self):
        return self.driver.find_elements(*HomePage.dropDownsName)

    def getTableHeader(self):
        return self.driver.find_element(*HomePage.tableHeader)

    # Access the WebTable
    def getTableData(self):
        return self.driver.find_elements(*HomePage.tableData)
