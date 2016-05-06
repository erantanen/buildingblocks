import pandas as pd


# http://pbpython.com/advanced-excel-workbooks.html
# http://xlsxwriter.readthedocs.io/working_with_pandas.html




def write_test(book):
    # Create a Pandas dataframe from the data.
    in_df = pd.DataFrame(
        dict(Data=[10, 20, 30, 20, 15, 30, 45],
             fqdn=['ichy.net','naa1','nan2', 'skipy.dorky.org','nan3','nan4','pfffft.burp.io']))

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(book, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    in_df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def write_test2(book):
    # Create a Pandas dataframe from some data.
    df = pd.DataFrame(zip(
        [1010, 2020, 3030, 2020, 1515, 3030, 4545],
        [.1, .2, .33, .25, .5, .75, .45],
        [.1, .2, .33, .25, .5, .75, .45],
    ))

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(book, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter objects from the dataframe writer object.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add some cell formats.
    format1 = workbook.add_format({'num_format': '#,##0.00'})
    format2 = workbook.add_format({'num_format': '0%'})
    format3 = workbook.add_format({'num_format': 'h:mm:ss AM/PM'})

    # Set the column width and format.
    worksheet.set_column('B:B', 18, format1)

    # Set the format but not the column width.
    worksheet.set_column('C:C', None, format2)

    worksheet.set_column('D:D', 16, format3)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def read_test(book):
    df = pd.read_excel(book, index_col=None, na_values=['NA'], parse_cols='B,C')

    return df




book = 'test.xlsx'

write_test(book)

print(read_test(book))