# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 01:25:29 2018

@author: a0309
"""

x, k= [int(x) for x in raw_input().split()]

MOD = 10 ** 9 + 7

def modulus(a, b, m):
    
    if b == 0:
        return 1
    if b == 1:
        return a % m
    
    result = int(modulus(a, b // 2, m))
    
    if b % 2 == 0:
        return  int (( (result % m) * (result % m) ) % m)
    else:
        return int (( (result % m) * (result % m) * (a % m)) % m)
    
def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
if x == 0:
    print(0)
elif k != 0:
    print( int( ( (modulus(2, k + 1, MOD) * (x % MOD) ) % MOD - (modulus(2, k, MOD)) % MOD + 1 + MOD) % MOD ))
else:
    print(int((x % MOD) * 2 % MOD) )