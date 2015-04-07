#-*- coding: utf-8 -*-
import chardet

result = []
f = open('data.txt', 'r')
for line in f.readlines():
	line = line.strip() #去掉空白符（包括'\n', '\r',  '\t',  ' ')
	if len(line) == 0 and line.startswith("#"):
		continue
	result.append(line)	
open('res.txt', 'w').write("%s"%"\n".join(result))
