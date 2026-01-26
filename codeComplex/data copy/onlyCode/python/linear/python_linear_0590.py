import math 

if __name__ == '__main__':
	
	n,q = [int(x) for x in raw_input().split()]
	qq = str(raw_input())
	s = [ int(x) for x in qq] 
	prefix = [0]*n
	prefix[0]= s[0]
	temp = [0]*(n+1)
	temp[0]=1
	mod = (pow(10,9)//1)+7
	for i in range(1,n):
		prefix[i] += prefix[i-1] + s[i]
		temp[i] =( 2*(temp[i-1]%mod) )%mod

	temp[n] = (2*(temp[n-1]%mod))%mod
	ansarr=[]
	while q> 0:
		q-=1
		l,r = [int(x)-1 for x in raw_input().split()]
		a = prefix[r]-prefix[l]+s[l]
		d = r-l+1
		val1 = temp[d] 
		val2 = temp[d-a] 
		# val2 = val2%mod
		ansarr.append((val1-val2)%mod)
	print('\n'.join(map(str, ansarr)))