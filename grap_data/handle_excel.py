#-*- coding: utf-8 -*-
import xlwt, xlrd

file_path = 'dest_excel.xls'
file_name = xlwt.Workbook()
sheet = file_name.add_sheet('dest_sheet', cell_overwrite_ok=True)
styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;'); # 80% like
sheet.write(1, 1, u'程品', styleBlueBkg)
sheet.write(2, 1, u'程品成品成品', styleBlueBkg)
# print len(u"程品成品成品")
# exit()
sheet.col(1).width = 256 * 100
# help(sheet.row(1))
file_name.save(file_path)

# data = xlrd.open_workbook(file_path)
# sheet = data.sheet_by_name("dest_sheet")
# sheet.put_cell(1, 1, 1, '程品', 0)
# print sheet.cell(1,1).value