#-*- coding: utf-8 -*-
import os, getopt
def cdWalker(path, res_file):
	result = ""
	for root, dirs, files in os.walk(path):
		result+="\n %s; %s; %s"%(root, dirs, files)
	open(res_file, 'w').write(result)

if __name__ == '__main__':
	CDROM = '/home/web_root/ottWeb/view'
	cdWalker(CDROM, "test2.cdc")