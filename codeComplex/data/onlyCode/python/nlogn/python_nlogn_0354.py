import sys,math
from collections import deque,defaultdict
import operator as op
from functools import reduce
from itertools import permutations
import heapq

#sys.setrecursionlimit(10**6) 
#OneDrive\Documents\codeforces

I=sys.stdin.readline

alpha="abcdefghijklmnopqrstuvwxyz"

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

	power=[2**i for i in range(32)]

	ans=[]
	
	
	for i in power:
		for j in arr:
			tmp=[j]
			for k in range(2):
				if tmp[-1]+i in sett:
					tmp.append(tmp[-1]+i)

			if len(tmp)>len(ans):
				# print(i,tmp,ans)
				ans=[x for x in tmp]

			if len(ans)==3:
				break

		if len(ans)==3:
			break

	print(len(ans))
	print(*ans)
















	








	




		
	

					

if __name__ == '__main__':
	main()