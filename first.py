import xlwt
import xlrd
import os

wkbk = xlwt.Workbook()
outsheet = wkbk.add_sheet('Sheet1')

folderPath = 'D:/files'
os.chdir(folderPath)

xlsfiles = [r'D:\foo.xlsx', r'D:\bar.xlsx', r'D:\baz.xlsx']

outrow_idx = 0
firstfile = True
for f in os.listdir(os.getcwd()):
    # This is all untested; essentially just pseudocode for concept!
    insheet = xlrd.open_workbook(f).sheets()[0]
    for row_idx in xrange(0 if firstfile else 1, insheet.nrows):
        pass  # processing; etc
        firstfile = False
        for col_idx in xrange(insheet.ncols):
            outsheet.write(outrow_idx, col_idx,insheet.cell_value(row_idx, col_idx))
        outrow_idx += 1
    os.remove(f)
wkbk.save(r'D:\combined.xls')
