#-*- coding: utf-8 -*-
import thread, time
mylock = thread.allocate_lock()#分配一个锁
num = 0 #共享资源

def add_num(name):
	global num
	while True:
		mylock.acquire() #获得这个锁
		#可以对共享资源进行处理
		print "Thread %s locked! num=%s"%(name, str(num))
		if num >=5:
			print "Thread %s released! num=%s"%(name, str(num))
			mylock.release()
			thread.exit_thread()
		num+=1
		print "Thread %s released! num=%s"%(name, str(num))
		mylock.release()  #释放锁
def test():
	thread.start_new_thread(add_num, ("a",))
	thread.start_new_thread(add_num, ("b",))

if __name__ == '__main__':
	test()