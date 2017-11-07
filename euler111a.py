# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:56:00 2016

@author: chris.mckinnon
"""
import math 

def genNbrs1(L,d):
    nbrs = []
    for j in range(0,L):
        for i in "0123456789":
            if i != d:
                nbrs.append(int(d*j + i + d*(L-1-j)))       
    return nbrs
   
def genNbrs2(L,d):
    nbrs = []                    
    for k1 in range(0, L-1):
        for i in "0123456789":
            if i != d:
                for k2 in range(0, L-k1-1):
                    for j in "0123456789":
                        if j != d:
                           nbrs.append(int(d*k1 + i + d*k2 + j + d*(L-k1-k2-2)))                
    return nbrs
    
def isprime(n):
    """Returns True if n is prime"""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
    
allTot = 0    
for d in "0123456789":
    tot = 0
    for n in genNbrs1(10,d):
        if n < math.pow(10,9): continue
        if isprime(n):
            tot += n
    if tot == 0:
        for n in genNbrs2(10,d):
            if n < math.pow(10,9): continue
            if isprime(n):
                tot += n
    print tot
    allTot += tot

print allTot
    