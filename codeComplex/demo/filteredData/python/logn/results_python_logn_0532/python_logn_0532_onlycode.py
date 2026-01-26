import math 
  
def countDigit(n): 
	return math.floor(math.log(n, 10)+1)



n=int(input())
count=countDigit(n)
if count==1:
	print(n)
else:
	low=1
	high=9
	sum=[]
	digit=0
	sum.append(0)
	sum.append(9)
	for i in range(2,16):
		low=low*10
		high=high*10+9
		#print(countDigit(high))
		sum.append((high-low+1)*i+sum[i-1])
		
		if n<sum[i]:
			digit=i
			break
	x=n-sum[digit-1]
	q=x/(digit)
	r=x%(digit)
	low=math.pow(10,digit-1)
	low=low+q-1
	#print(low)
	if r==0:
		print(int(low%10))
	else:
		n=low+1
		stringnum=str(n)
		print(int(stringnum[r-1]))