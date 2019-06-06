#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;

def i2osp(x):
	result = []
	for y in range(3):
		result.append(int (x%256))
		x/=256
	return result

chaves=[]
file = open('chaves', 'r')
for line in file:
	chaves.append(int(line))
file.close()


decifrado=[]
file = open(str(sys.argv[1]), 'r') 

for line in file: 
	block = int(line)	
	decifrado.append(pow(block, chaves[0], chaves[1]))
file.close()


file = open(str(sys.argv[2]), 'w') 
for x in range(0,len(decifrado)):
	result = i2osp(decifrado[x])
	for y in xrange(0, len(result)):
		file.write(chr(result[y]))
file.close()

