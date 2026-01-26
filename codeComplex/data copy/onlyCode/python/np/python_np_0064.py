from math import factorial as fact
s1 = input()
s2 = input()
plus1 = s1.count("+")
minus1 = s1.count("-")

plus2 = s2.count("+")
minus2 = s2.count("-")
qCount = s2.count("?")

if(plus1==plus2 and minus1==minus2):
	print(1)
else:
	plusReq = plus1 - plus2
	minusReq = minus1 - minus2
	if(plusReq >= 0 and minusReq >= 0):
		ans = (0.5**qCount)*fact(qCount)/(fact(plusReq)*fact(minusReq))
		print(ans)
		
	else:
		print(0)
