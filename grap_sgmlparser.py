#-*-coding: utf-8 -*-
import urllib2, xlwt, xlrd
from sgmllib import SGMLParser

class ListName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_a = ""
		self.name = []
		self.singer = []
	def start_a(self, attrs):
		href = [v for k, v in attrs if k == 'href']
		if str(href).find('/song/') != -1:
			self.is_a = 1
	def start_span(self, attrs):
		if len(attrs) == 2 and attrs[0][0] == "class" and attrs[0][1] == "author_list":
			self.singer.append(attrs[1][1])
	def end_a(self):
		self.is_a = ""
	def handle_data(self, text):
		if self.is_a == 1:
			self.name.append(text)	
content = urllib2.urlopen('http://music.baidu.com/top/dayhot').read()
listname = ListName()
listname.feed(content.replace("&#039;", "'"))
print len(listname.name)
print len(listname.singer)
i = 0
for song_name in listname.name:
	open('result_sgmlparser.txt', 'a').write(song_name + '    ' + listname.singer[i] + "\n")
	i = i + 1

#将数据写入xls中
#创建一个空文件
des_file = xlwt.Workbook()
sheet = des_file.add_sheet('song_infos', cell_overwrite_ok=True)
#向空文件中写一个表头,并设置样式
styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;'); # 80% like
sheet.write(0, 0, u'歌曲名', styleBlueBkg)
sheet.write(0, 1, u'歌手', styleBlueBkg)

col = 1
for song_name in listname.name:
	sheet.write(col, 0, song_name.decode('utf-8'))
	sheet.write(col, 1, listname.singer[col-1].decode('utf-8'))
	#设置列宽
	sheet.col(0).width = 256*40    
	sheet.col(1).width = 526*15
	col = col + 1
des_file.save('song_infos.xls')

	
