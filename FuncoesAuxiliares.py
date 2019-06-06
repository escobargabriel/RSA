#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from random import randint
import time
import math
from fractions import gcd

def fermat(n):
	if n == 2:
		return True	   
	for i in xrange(30):
		a = random.randint(1, n-1)
		if pow(a, n-1, n) != 1:
			return False
	return True


def numerosPrimos(bits):
	NumerosPrimos=[]
	counter=0
	while (counter < 3):
		flag=0
		number = random.getrandbits(bits)
		if (number%2==0):
			number+=1
		while (flag==0):							
			if (fermat(number)):
				if (counter == 0 or number!= NumerosPrimos[counter-1]):
					NumerosPrimos.append(number)
					flag = 1
			else:
				number+=2
		counter+=1
	return NumerosPrimos	

def euclidesExt(e, qq):
	if e == 0:
		return (qq, 0, 1)
	else:
		g, x, y = euclidesExt(qq % e, e)
		return (g, y - (qq // e) * x, x)

def invMul(e, qq):
	g, x, _ = euclidesExt(e, qq)
	if g == 1:
		return x % qq

def os2ip(lista):
	x = 0;
	for i in range(0, len(lista)):
		x += lista[i]*256**i

	return x;

def leArquivo(filename):
	f = open(filename, 'rb')
	blocks = []
	byte = f.read(3)
	blocks.append(os2ip([ord(c) for c in byte]))
	counter = 0
	while byte:
		counter+=1	
		byte = f.read(3)	
		if (len([ord(c) for c in byte]) < 3 and len([ord(c) for c in byte]) == 2):
			a = [ord(c) for c in byte]
			test = []
			test.extend([ord(c) for c in byte])		
			test.append(32)
			blocks.append(os2ip(test))
		if (len([ord(c) for c in byte]) < 3 and len([ord(c) for c in byte]) == 1):
			a = [ord(c) for c in byte]
			test = []
			test.extend([ord(c) for c in byte])
			test.append(32)
			test.append(32)
			blocks.append(os2ip(test))
		if (len([ord(c) for c in byte]) == 3 ):			
			blocks.append(os2ip([ord(c) for c in byte]))
	#print blocks

	return blocks

def salvaChaves(filename, d, n):
	file = open(filename, 'w')
	file.write("%d\n" % d)
	file.write("%d\n" % n)
	file.close()

def writeFile(filename, listadeBlocos):
	file = open(filename, "w")
	for x in range(0,len(listadeBlocos)):		
		file.write("%d\n" % listadeBlocos[x])
	file.close()

def geraChavesTempo():
	temp, bits = [],[]
	for x in xrange(4, 13):
		begin = time.time()
		numerosPrimos(2**x)		
		end = time.time() - begin		
		temp.append(end)
		bits.append(2**x)
	import matplotlib.pyplot as plt 
	plt.plot(bits, temp)
	plt.xlabel("Bits")
	plt.ylabel("Tempo (s)")
	plt.show()

def pollards_rho(n, seed=2, f=lambda x: x**2 + 1):
   x, y, d = seed, seed, 1
   while d == 1:
     x = f(x) % n
     y = f(f(y)) % n
     d = gcd((x - y) % n, n)
   return None if d == n else d

def PollardsTempo(lista):
	temp, bits = [],[]
	while (len(lista)!=0):
		n = lista.pop()		
		begin = time.time()
		pollards_rho(n)		
		end = time.time() - begin
		temp.append(end)
		bits.append(int(math.log(n, 2)+1))
	import matplotlib.pyplot as plt 
	plt.plot(bits, temp)
	plt.xlabel("Bits")
	plt.ylabel("Tempo (s)")
	plt.show()


			

if __name__ == '__main__':
	lista = [229737846920514198987443907486316029203]
	#geraChavesTempo()
	PollardsTempo(lista)
