"""
Brandt Smith, Lemuel Gorion and Peter Haddad

codeforces.com

Problem 12455
"""
import sys

def set(mask, pos):
    return mask | (1 << pos)

def isOn(mask, pos):
    return mask & ( 1 << pos) > 0

n, l, r, x = map(int, input().split(' '))
dif = list(map(int, input().split(' ')))

count, mask = 0, 0

while mask <= 2**n:
    summ, bit = [], 0

    while bit < n:
                
        if isOn(mask, bit):
            summ.append(dif[bit])
                    
        bit += 1
        
    if sum(summ) <= r and sum(summ) >= l and max(summ) - min(summ) >= x:
        count += 1
                
    mask += 1
                
                
print(count)

    
    

