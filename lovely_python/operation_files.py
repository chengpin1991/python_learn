#-*- coding: utf-8 -*-
import os, getopt, sys
path = ""
des_file = ""
find_path = []
def getfiles(path, des_file):
	export = ""
	for root, dirs, files in os.walk(path):
		export += "\n %s %s %s"%(root, dirs, files);
	open(des_file, 'w').write(export)	

if __name__ == "__main__":
	# getfiles('/home/web_root/ottWeb/view', 'res.txt')
	try:
		opts, args = getopt.getopt(sys.argv[1:], "p:e:k:f:")
	except getopt.GetoptError:
		exit()
	if len(opts) == 0:
		exit()

	for opt, arg in opts:
		if opt == "-p":    #指定需要查找的目标路径
			path = arg
		elif opt == "-e":  #将文件写入当前位置
			des_file = arg
			getfiles(path, arg)
		elif opt == "-k":   #将文件写入指定位置
			index = len(arg.split("/")[-1]) +1 
			cmd = "mkdir -p " + arg[:-index]
			if os.system(cmd) == 0:
				des_file = arg
				getfiles(path, arg)
		elif opt == "-f": #查看目录中包含指定字符的具体位置
			getfiles(path, des_file)
			s = open(des_file, 'r').readlines()
			for line in s:
				if line.find(arg) != -1:
					find_path.append(line)
			print find_path		

