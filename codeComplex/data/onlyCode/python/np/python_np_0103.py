from itertools import permutations,combinations
from math import factorial
word1 = list(map(str,input()))
word2 = list(map(str,input()))
expected = 0
for i in word1:
    if i=='+':
        expected+=1
    else:
        expected-=1
blank = 0
for i in word2:
    if i=='+':
        expected-=1
    elif i=='-':
        expected+=1
    else:
        blank+=1
if abs(expected)>blank:
    print(float(0))
elif blank==0:
    if expected==0:
        print(1)
    else:
        print(0)
else:
    total = 2**blank
    if expected==blank-1:
        print(float(0))
    else:
        f = (blank-expected)//2
        if expected>0:
            a,b = expected+f,f
        elif expected<0:
            a,b = expected+f,f
        else:
            a,b = f,f
        ans = factorial(a+b)/(factorial(a))
        ans = ans/factorial(b)
        ans = ans/total
        print(ans)