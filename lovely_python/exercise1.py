#-*- coding: utf-8 -*-
import os
#原始
for root, dirs, files in os.walk('D:\\Python26\\python_learn'):
	open('file_data.txt', 'a').write("%s \n %s\n %s\n"%(root, dirs, files))

#改进
export = ""
for root, dirs, files in os.walk('D:\\Python26\\python_learn'):	
	export+="%s \n %s\n %s\n"%(root, dirs, files)
open('file_data1.txt', 'w').write(export)

#再改进
export = []
for root, dirs, files in os.walk('D:\\Python26\\python_learn'):	
	export.append("%s \n %s\n %s\n"%(root, dirs, files))
open('file_data2.txt', 'w').write("".join(export))

#字符串join要比+操作效率高。因为对象反复+，比一次性内建处理，要浪费资源