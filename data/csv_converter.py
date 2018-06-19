import xlrd
import unicodecsv as csv

CoC = '2007-2017-PIT-Counts-by-CoC.XLSX'
state = '2007-2017-PIT-Counts-by-State.xlsx'

def csv_from_excel(wrkbk,csv_name):
    wb = xlrd.open_workbook(wrkbk)
    sh = wb.sheet_names()
    for name in sh:
    	full_csv_name = csv_name + name + '.csv'
    	csv_file = open(full_csv_name, 'w')
    	wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    	sheet = wb.sheet_by_name(name)

        for rownum in range(sheet.nrows):
            wr.writerow(sheet.row_values(rownum))

        csv_file.close()

csv_from_excel(CoC,'CoC')
csv_from_excel(state,'state')
