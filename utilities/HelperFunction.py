#! /usr/bin/python

sorting_implemented = ['NUMBER OF CASES', 'COMPLEXITY']


def validate_element(selected_header, table_headers):
    if str(selected_header).upper() in table_headers:
        return True
    else:
        return False

def categorySort(default_list, column_index):
    category = dict(low=0, medium=1, high=2)
    default_list.sort(key=lambda x: category[(x[column_index])],reverse=False)
    return default_list


def averageSort(default_list, column_index):
    value = sorted(default_list, key=lambda x: (int(float(x[column_index]))), reverse=False)
    return value


def sorting_column(default_list, column_index):
    for ele in default_list:
        if 'k' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('k')) * 1000
        elif 'M' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('M')) * 1000000
        elif 'M' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('B')) * 1000000000
        else:
            ele[column_index] = int(ele[column_index])
    return sorted(default_list, key=lambda x: x[column_index])


def frameData(sortedlist, column_index):
    for ele in sortedlist:
        if 'k' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('k')) * 1000
        elif 'M' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('M')) * 1000000
        elif 'M' in ele[column_index]:
            ele[column_index] = float(ele[column_index].rstrip('B')) * 1000000000
        else:
            ele[1] = int(ele[column_index])
    return sortedlist


def sortSortedData(sorted_by_column):
    if str(sorted_by_column).upper() == "COMPLEXITY":
        return True
    else:
        return False


def checkSortByHeader(sorted_by_column):
    if str(sorted_by_column).upper() == "NUMBER OF CASES":
        return True
    else:
        return False


def selectSortingMethod(sorted_by_column, default_list, column_index):
    if str(sorted_by_column).upper() == "NUMBER OF CASES":
        number_of_case = sorting_column(default_list, column_index)
        return number_of_case
    elif str(sorted_by_column).upper() == "COMPLEXITY":
        return categorySort(default_list, column_index)
    else:
        otherColumnHeader = averageSort(default_list, column_index)
        return otherColumnHeader


# function to check whether the list is empty or not
def is_list_empty(default_list):
    if len(default_list) == 0:
        return 0
    else:
        return 1


def checkWebListLength(default_list):
    if len(default_list) == 1 or len(default_list) == 0:
        return 0
    else:
        return 1


def getIndexColumn(list_of_headers, select_column_dropdown):
    index = ""
    # headerCount= len(list_of_headers)
    for element in list_of_headers:
        if element == str(select_column_dropdown).upper():
            index = list_of_headers.index(element)
            break
    return index


def countTotalDropdownAndColumn(Dropdowns, Columns):
    len_of_dropdown = len(Dropdowns)
    len_of_column = len(Columns)
    if len_of_dropdown == len_of_column:
        return True


def getSortingMethod(selected_column):
    if selected_column in sorting_implemented:
        return True
    else:
        return False
