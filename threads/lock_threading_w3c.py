#-*- coding: utf-8 -*-
import threading, time
mylock = threading.RLock()

class myThread(threading.Thread):
	def __init__(self, name, delay, counter):
		super(myThread, self).__init__()
		self.name = name
		self.delay = delay
		self.counter = counter
		self.isstop = False

	def print_time(self, name, delay, counter):
		while not self.isstop:
			time.sleep(delay)
			print "%s: %s \n"%(name, time.ctime())
			counter-=1
			if counter <= 0:
				self.isstop = True

	def run(self):
		print "\nStarting " + self.name
		mylock.acquire()
		self.print_time(self.name, self.delay, self.counter)
		mylock.release()

	


thread1 = myThread("A", 2, 3)
thread2 = myThread("B", 1, 3)
threads = []
threads.append(thread1)
threads.append(thread2)
for thread in threads:
	thread.start()

#等待所有线程执行完
for thread in threads:
	thread.join()    

print "Existing Main Thread\n"