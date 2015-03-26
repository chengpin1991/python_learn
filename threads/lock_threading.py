#-*- coding: utf-8 -*-
import threading
mylock = threading.RLock()
num = 0

class myThread(threading.Thread):
	def __init__(self, name):
		super(myThread, self).__init__()
		self.name = name

	def run(self):
		global num	
		while True:
			mylock.acquire()
			print "Thread (%s) locked!, Number: %d"%(self.name, num)
			if num >5:
				print "Thread (%s) released!, Number: %d"%(self.name, num)
				break
			num+=1
			print "Thread (%s) released!, Number: %d"%(self.name, num)
			mylock.release()

def test():
	thread1 = myThread('A')
	thread2 = myThread('B')
	thread1.setDaemon(True)
	# thread2.setDaemon(True)
	thread1.start()
	thread2.start()


if __name__ == '__main__':
	test()
