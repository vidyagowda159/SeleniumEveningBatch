# pip install xlrd==1.2.0
import xlrd

# open the excel workbook
workbook = xlrd.open_workbook("emp_details.xlsx")

# get the sheet using the sheetname
worksheet = workbook.sheet_by_name("Sheet1")

# access all the rows
rows = worksheet.get_rows()        # generator object

header = next(rows)

# for row in rows:
# 	print(row[0].value, row[1].value)      # list of cell objects

data = {row[0].value: row[1].value for row in rows}
print(data)

# number of used columns
print(worksheet.ncols)

# number of used rows
print(worksheet.nrows)
