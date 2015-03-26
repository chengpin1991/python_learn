#-*- coding: utf-8 -*-
import time, threading
class timer(threading.Thread):#类timer继承至threading.Thread
	def __init__(self, num, interval):
		super(timer, self).__init__()
		self.thread_num = num
		self.interval = interval
		self.thread_stop = False

	def run(self):#重写父类的run()方法
		while not self.thread_stop:
			print "Thread Object %d, Time:%s"%(self.thread_num, time.ctime())
			time.sleep(self.interval)
    
	def stop(self):
		self.thread_stop = True

def test():
	thread1 = timer(1, 5)
	thread2 = timer(2, 3)
	thread1.start()
	thread2.start()
	time.sleep(10)
	thread1.stop()
	thread2.stop()

if __name__ == '__main__':
	test()
