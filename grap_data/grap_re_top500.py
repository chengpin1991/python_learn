#-*- coding: utf-8 -*-
import urllib, sys, re, xlwt
reload(sys)
sys.setdefaultencoding('utf-8')
response = urllib.urlopen('http://music.baidu.com/top/dayhot')
source = response.read().decode('utf-8')
singers_list = re.findall(ur'<span\sclass="author_list"\stitle="(.+)">', source)
song_names = []
songs_list = re.findall(ur'<a.*/song/\d+.*>.*</a>', source)
for a in songs_list:
	try:
		song_name = re.findall(ur'<a[^>]*>([^<]*)</a>', a.encode('utf-8', 'ignore').decode('utf-8'))
		if song_name != '':
			song_names.append(song_name[0])
	except:
		print 'ERROR'

while '' in song_names:
	song_names.remove('')

while '' in singers_list:
	singers_list.remove('')


#将数据写入xls中
#创建一个空文件
des_file = xlwt.Workbook()
sheet = des_file.add_sheet('song_infos', cell_overwrite_ok=True)
#向空文件中写一个表头,并设置样式
styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;'); # 80% like
sheet.write(0, 0, u'歌曲名', styleBlueBkg)
sheet.write(0, 1, u'歌手', styleBlueBkg)

col = 1
for song_name in song_names:
	sheet.write(col, 0, song_name.decode('utf-8'))
	sheet.write(col, 1, singers_list[col-1].decode('utf-8'))
	#设置列宽
	sheet.col(0).width = 256*40    
	sheet.col(1).width = 526*15
	col = col + 1
des_file.save('song_infos.xls')