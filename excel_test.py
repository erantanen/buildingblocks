import pandas as pd






with pd.ExcelFile('test.xls') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')

print("------------\n")

print(type(df1))

print("------------\n")

print(df1)