#-*- coding: utf-8 -*-
import sys, os, cmd
class PyCDC(cmd.Cmd):
	def __init__(self):
		super(PyCDC, self).__init__();
	def help_EOF(self):
		print "退出程序 quits the program"
	def do_EOF(self, line):
		sys.exit();
	def help_dir(self):
		print "指定保存/搜索目录"
	def do_dir(self, pathname):
		if pathname == "": pathname = raw_input("输入指定保存/搜索目录：")
	def help_find(self):
		print "搜索关键字"
	def do_find(self, keyword):
		if keyword == "": keyword = raw_input("输入搜索关键字：")
		print "搜索关键字：%s"%keyword

if __name__ == "__main__":
	cdc = PyCDC()
	cdc.cmdloop()
