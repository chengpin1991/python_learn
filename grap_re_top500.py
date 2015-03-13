#-*- coding : utf-8 -*-
import urllib, sys, re, HTMLParser
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
i = 0
for song_name in song_names:
	open('result', 'a').write(song_name.encode('utf-8', 'ignore') + '        ' + singers_list[i].encode('utf-8', 'ignore') + "\n")
	i = i + 1


