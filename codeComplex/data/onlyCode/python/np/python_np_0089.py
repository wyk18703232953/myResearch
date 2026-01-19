import math
s1=input()
s2=input()
dist=0
pos=0
unrecognized=0
for i in s1:
	if i =="+":
		dist+=1
	else:
		dist-=1

for i in s2:
	if i =="+":
		pos+=1
	elif i=="-":
		pos-=1
	elif i=="?":
		unrecognized+=1
difference=dist-pos

if abs(difference)>abs(unrecognized):
	print("{0:.9f}".format(float(0)))
else:
	extra=unrecognized-abs(difference)
	perm_extra=1
	for i in range(1,unrecognized+1):
			perm_extra=perm_extra*i
	perm_extra=perm_extra/(math.factorial(extra/2+(unrecognized-extra))*math.factorial(extra/2))
	if extra%2!=0:
		print("{0:.9f}".format(float(0)))
	else:
		print("{0:.9f}".format(float(perm_extra*(0.5**unrecognized))))


		 				 		  	  	 	     	  			