import math
def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)
dict1 = {'+':0,'-':0,'?':0}
for i in input():
	dict1[i]+=1
for i in input():
	if(i=='?'):
		dict1[i]+=1
	else:
		dict1[i]-=1
if dict1['+']<0 or dict1['-']<0:
	print(0.000000000000)
elif dict1['+']==0 and dict1['-']==0:
	print(1.000000000000)
elif dict1['+'] and dict1['-']:
	ans = (nCr(dict1['?'], dict1['+'])/(2**dict1['?']))
	print("%.12f" %ans)
else:
	ans = (1 / (2 ** dict1['?']))
	print("%.12f" % ans)