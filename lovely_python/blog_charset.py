#-*- coding: utf-8 -*-
import urllib2, chardet
source = urllib2.urlopen("http://blog.sina.com.cn/s/articlelist_1642668115_0_1.html").read()
# print chardet.detect(source)
charset = chardet.detect(source)["encoding"]
try:
	source = unicode(source, charset)
	source = source.encode('utf-8')
except:
	print u"bad unicode encode try!"
