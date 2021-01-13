import xlrd
import os


class Read():
    workbook = xlrd.open_workbook("C:/Users/pct131/PycharmProjects/PytestDemo/TestData/Datafile.xls")
    sheet = workbook.sheet_by_name("login")

    rowCount = sheet.nrows
    colCount = sheet.ncols

    for curr_row in range(1, rowCount):
        username = sheet.cell_value(curr_row, 0)
        password = sheet.cell_value(curr_row, 1)

