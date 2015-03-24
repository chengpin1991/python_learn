#-*- coding: utf-8 -*-
from time import ctime, sleep

def music():
    for i in range(2):
	print "I was listening to music. %s"%ctime()
	sleep(7)

def movie():
    for i in range(2):
	print "I was watching a movie.%s"%ctime()
	sleep(1)

if __name__ == '__main__':
     music()
     movie()
     print "all over at %s"%ctime()
