#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;
from FuncoesAuxiliares import leArquivo
from FuncoesAuxiliares import fermat
from FuncoesAuxiliares import numerosPrimos
from FuncoesAuxiliares import invMul
from FuncoesAuxiliares import salvaChaves
from FuncoesAuxiliares import writeFile

primesList=[];
primesList = numerosPrimos(int(sys.argv[3]))
print str(primesList[0])
print str(primesList[1])
n   = primesList[0]*primesList[1]
qq = (primesList[0]-1)*(primesList[1]-1)
d   = invMul(primesList[2], qq)


salvaChaves('chaves', d, n)
print 'Geradas as chaves publica e privada'

blocks = []
blocks = leArquivo(str(sys.argv[1]))
cryptedBlocks = []
for x in xrange(0,len(blocks)):
	cryptedBlocks.append(pow(blocks[x], primesList[2], n))
writeFile(str(sys.argv[2]), cryptedBlocks)

#print str("p ")+str(primesList[0])
#print str("q ")+str(primesList[1])
#print str("e ")+str(primesList[2])
#print str("d ")+str(d)
#print str("n ")+str(n)

