from sys import stdin, stdout

def binary_exp(x,n,prime): #calculate x^n%p
	if n==0:
		return 1
	elif n==1:
		return x%prime
	else:
		temp=binary_exp(x,n//2,prime)
		temp=(temp*temp)%prime
		if n%2==0:
			return temp
		else:
			return ((x%prime)*temp)%prime

x,k = map(int, stdin.readline().rstrip().split())
if x==0:
	print(0)
else:
	val1=binary_exp(2,k+1,1000000007)
	val2=binary_exp(2,k,1000000007)
	val1=val1%1000000007
	val2=val2%1000000007
	#print(val1,val2)
	ans=((val1*(x%1000000007))%1000000007 -(val2-1)%1000000007)%1000000007
	print(ans)