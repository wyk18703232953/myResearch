import math
send=input()
rcv=input()
d={}
d['+']=0
d['-']=0
for i in range(len(send)):
	d[send[i]]=d[send[i]]+1

flag=1
c=0
for i in range(len(rcv)):
	if rcv[i] in d:
		if d[rcv[i]]==0:
			flag=0
		else:
			d[rcv[i]]=d[rcv[i]]-1
tot=d['+']+d['-']
totComb=2**tot
n=tot
r=d['+']
npr=math.factorial(n)/math.factorial(n-r)
reqComb=npr/math.factorial(r)
#print(totComb)
#print(reqComb)
if flag==0:
	print('0.00000000')
else:
	print(float(reqComb)/totComb)