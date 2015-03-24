#-*- coding: utf-8 -*-
from selenium import webdriver
import xlwt
singer_lists = []
song_name_list = []
driver = webdriver.PhantomJS()
driver.get("http://music.baidu.com/top/dayhot") 
song_name_res = driver.find_elements_by_xpath("//span[@class='song-title ']/a[1]")
for song_name_single in song_name_res:
	song_name_list.append(song_name_single.text)

base_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 2
for i in base_list:
	driver.find_element_by_class_name("page-navigator-next").click()
	i = i + 1
	song_name_res = driver.find_elements_by_xpath("//span[@class='song-title ']/a[1]")
	for song_name_single in song_name_res[-50:]:
		song_name_list.append(song_name_single.text)
res = driver.find_elements_by_class_name("author_list")
for a in res:
	singer_lists.append(a.get_attribute("title").encode('utf-8', 'ignore'))
print len(singer_lists)
print len(song_name_list)

#将数据写入xls中
#创建一个空文件
des_file = xlwt.Workbook()
sheet = des_file.add_sheet('song_infos', cell_overwrite_ok=True)
#向空文件中写一个表头,并设置样式
styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;'); # 80% like
sheet.write(0, 0, u'歌曲名', styleBlueBkg)
sheet.write(0, 1, u'歌手', styleBlueBkg)

col = 1
for song_name in song_name_list:
	sheet.write(col, 0, song_name)
	sheet.write(col, 1, singer_lists[col-1].decode('utf-8', 'ignore'))
	#设置列宽
	sheet.col(0).width = 256*40    
	sheet.col(1).width = 526*15
	col = col + 1
des_file.save('song_infos.xls')