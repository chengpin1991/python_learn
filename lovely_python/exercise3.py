#-*- coding: utf-8 -*-
import os, getopt
def cddirs(path, res_file):
	result = ""
	for root, dirs, files in os.walk(path):
		result+="\n %s %s %s"%(root, dirs, files)
	open(res_file, 'w').write(result)

def usage():
	print '''使用方式
	python exercise3.py -d cdc -k 中国火
	#搜索cdc目录中的光盘信息，寻找"中国火"字样的文件或是目录，在哪张光盘
	'''

try:
	opts, args = getopt.getopt(sys.argv[1:], 'd:e:k:')
except getopt.GetoptError:
	usage()
	sys.exit()
if len(opts) == 0:
	usage()
	sys.exit()

for opt, arg in opts:
	if opt == '-d':
		#
	elif opt == '-e':
		#
	else:
		#
if __name__ == "__main__":
	cddirs("D:\\Python26\\python_learn\\lovely_python", 'text.cdc')