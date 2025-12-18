#476B
from math import factorial as fact
s=input()
t=input()
pos=s.count('+')-t.count('+')
neg=s.count('-')-t.count('-')
que=t.count('?')
if pos<0 or neg<0:
    print(0)
else:
    print((fact(que)/(fact(pos)*fact(neg)))/(2**que))