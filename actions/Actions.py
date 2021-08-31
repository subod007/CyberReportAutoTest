#! /usr/bin/python

from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.HelperFunction import *


class Actions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def clear(self, element):
        element.clear()

    def sendKeys(self, element, value):
        element.send_keys(value)

    def selectFromDD(self, dropdown, value):
        dd_element = Select(dropdown)
        dd_element.select_by_value(value)

    def getText(self, element):
        return element.text

    def getTitle(self):
        return self.driver.title


    def getTextBox(self,element):
        return element.click

    def selectDropDown(self, element):
        selector = Select(element)
        options = selector.options
        return options

    def selectDropDownList(self, element):
        selector = Select(element)
        listOption = selector.select_by_visible_text("Number of cases")
        return listOption

    def selectedDropDown(self, element):
        dropdown = Select(element)
        default_option = dropdown.first_selected_option
        return default_option.text

    def selectAllDropDown(self, elements):
        # find the options
        opts = []
        for o in elements:
            opts.append(o.text)
        return opts

    def getTableHeader(self, element):
        header = element.text
        headers = header.split('\n')
        return headers

    def getTableData(self, elements):
        valueList = []
        for row in elements:
            value = row.text
            valList = value.split("\n")
            valueList.append(valList)
        return valueList


    def columnSelectToSort(self,select_column_header,element):
        selector = Select(element)
        dropdown=selector.select_by_visible_text(select_column_header)

    def enterTextInFilterBox(selectColumnHeader,element):
        assert is_list_empty(selectColumnHeader) == 1, "Add column name into the input data file!"
        element.click()


    # def selectDropDownList(self, element,select_dropdown):
    #     selector = Select(element)
    #     selector.select_by_visible_text(select_dropdown)