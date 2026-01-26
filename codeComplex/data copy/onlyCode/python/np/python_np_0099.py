import sys
import math
input=sys.stdin.readline
a=list(input())
b=list(input())
x=a.count('+')-b.count('+')
y=a.count('-')-b.count('-')
if x<0 or y<0:
    print(0)
else:
    fact=math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
    total=2**(x+y)
    print(fact/total)

			 	    	  	  		    	   	 	  	