#-*- coding: utf-8 -*-
import sys

dic = {}
f = open('./cdays-test.txt', 'r')
for line in f.readlines():
	data = line.strip('\n').split(' ')
	if data[1] in dic:
		dic[data[1]].append(data[0])
	else:
		dic[data[1]] = [data[0]]
print str(dic).replace(':', "=>")