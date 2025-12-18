import sys,math
from collections import deque,defaultdict
import operator as op
from functools import reduce
from itertools import permutations

#sys.setrecursionlimit(10**6) 

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

"""def ncr(n, r):
    r = min(r, n-r)
    numer = (reduce(op.mul, range(n, n-r, -1), 1))%(10**9+7)
    denom = (reduce(op.mul, range(1, r+1), 1))%(10**9+7)
    return (numer // denom)%(10**9+7)"""
def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, 
            p - 2, p)) % p
 

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def valid(row,col,rows,cols,rcross,lcross):
 	return rows[row]==0 and cols[col]==0 and rcross[col+row]==0 and lcross[col-row]==0


def div(n):
	if n==1:
		return 1
	cnt=2
	for i in range(2,int(n**.5)+1):
		if n%i==0:			
			if i!=n//i:
				cnt+=2
			else:
				cnt+=1
	return cnt

	

def isPrime(n):
	if n<=1:
		return False
	elif n<=2:
		return True
	else:
		flag=True
		for i in range(2,int(n**.5)+1):
			if n%i==0:
				flag=False
				break
		return flag

def s(b):
	ans=[]
	while b>0:
		tmp=b%10
		ans.append(tmp)
		b=b//10
	return ans



def main():
	n,k=mi()
	arr=[]
	for _ in range(n):
		x,y=mi()
		arr.append((x,y))

	arr=sorted(arr,key=lambda x: x[0],reverse=True)
	
	for i in range(n-1):
		for j in range(i+1,n):
			if arr[i][0]==arr[j][0] and arr[i][1]>arr[j][1]:
				arr[i],arr[j]=arr[j],arr[i]

	#print(arr)
	cnt=arr.count(arr[k-1])
	print(cnt)


		


		


			
		
	









					
		
		





		








	

	


 
	
	








	



	
		




	










	


	

	

		



		

		
		


	
	

		
	

		




		




			












			
		
			



		


	
			
						
			








	





			
		



	
			





	

























	
	
	





if __name__ == '__main__':
	main()