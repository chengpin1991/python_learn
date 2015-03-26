#-*- coding: utf-8 -*-
#函数式：调用thread模块中的start_new_thread()函数来产生新线程

import time, thread
def timer(no, interval):
	i = 0
	while i < 10:
		print "Thread:(%d) Time:%s"%(no, time.srtftime("%F %T"))
		time.sleep(interval)
		i+=1
	thread.exit_thread()	

def test():#使用thread.start_new_thread()来创建2个新线程
	thread.start_new_thread(timer, (1, 2))
	thread.start_new_thread(timer, (2, 2))


if __name__ == '__main__':  #表示是否以python moudule_thread.py的方式来执行代码
	test()