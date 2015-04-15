#-*- coding: utf-8 -*-
class Stack:
	def __init__(self, max):
		self.head = 0
		self.stack = []
		self.max = max

	def put(self, item):
		print self.stack
		print self.head
		if self.head >= self.max:
			print  'put error:the stack is overflow'
			return 
		else:
			self.head += 1
			self.stack.append(item)
			print "put %s success" % item
	def get(self):
		if self.head <= 0:
			print "get error: the stack is empty" 
		else:
			self.head -= 1
			print "get %s success" % self.stack[-1:]
			self.stack.pop()
			return

if __name__ == '__main__':
	mystack = Stack(5)
	mystack.put(1)
	mystack.put(2)
	mystack.put(3)
	mystack.put(4)
	mystack.put(5)
	# mystack.put(6)
	mystack.get()
	mystack.get()
	mystack.get()
	mystack.get()
	mystack.get()
	mystack.get()