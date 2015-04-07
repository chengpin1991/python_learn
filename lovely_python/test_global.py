#-*- coding: utf-8 -*-
a1 = 5

def func1():
	global a1 
	a1 = a1+5
	return a1

def func2():
	global a1
	b1 = a1
	print b1

if __name__ == "__main__":
	func1()
	func2()