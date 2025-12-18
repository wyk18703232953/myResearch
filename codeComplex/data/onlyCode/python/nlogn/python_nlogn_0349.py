import sys,math
from collections import deque,defaultdict
import operator as op
from functools import reduce
from itertools import permutations

#sys.setrecursionlimit(10**4) 
#C:\Users\bittu\OneDrive\Documents\codeforces
I=sys.stdin.readline

#alpha="abcdefghijklmnopqrstuvwxyz"

"""
x_move=[-1,0,1,0,-1,1,1,-1]
y_move=[0,1,0,-1,1,1,-1,-1]
"""
def ii():
	return int(I().strip())
def li():
	return list(map(int,I().strip().split()))
def mi():
	return map(int,I().strip().split())


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 
 

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def isPrime(n):
	if n<=1:
		return False
	elif n<=2:
		return True
	else:
		
		for i in range(2,int(n**.5)+1):
			if n%i==0:
				return False
		return True

#print("Case #"+str(_+1)+":",abs(cnt-k))




def main():
	n=ii()
	arr=li()
	sett=set(arr)
	ans=[arr[0]]
	flag=0
	for x in range(31):
		for i in arr:
			if (i-2**x) in sett and (i+2**x) in sett:
				ans=[i-2**x,i,i+2**x]
				flag=1
				break
			elif i-2**x in sett:
				ans=[i-2**x,i]
			elif i+2**x in sett:
				ans=[i,i+2**x]
			


		if flag:
			break
	print(len(ans))
	print(*ans)


		



	

	

	

	




			

	





	








							





		

	

	

		
				
					

		




		










	






		

	



	








		
			





		






	

if __name__ == '__main__':
	main()