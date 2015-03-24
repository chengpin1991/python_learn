#-*- coding: utf-8 -*-
from time import ctime, sleep
import threading

def music(name):
	for i in range(2):
		print "I was listening to %s. %s"%(name, ctime())
		sleep(7)

def movie(name):
	for i in range(2):
		print "I was watching a movie %s. %s"%(name, ctime())
		sleep(1)

threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
t2 = threading.Thread(target=movie, args=(u'阿凡达',))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
#	music(u'爱情买卖')
#	movie(u'阿凡达')
	for t in threads:
		t.setDaemon(True)
		t.start()
		t.join()
	print "all over %s"%ctime()

