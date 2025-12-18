from math import factorial,pow
send = input()
received = input()

pos = 0
for p in send:
	pos = pos +1 if p=='+' else pos-1
qcount = 0
curr_pos = 0
for p in received:
	if p=='+':
		curr_pos = curr_pos +1  
	elif(p=='-'):
		curr_pos = curr_pos-1
	if p=='?':
		qcount +=1

if qcount == 0:
	print("{:.12f}".format(1.0 if pos==curr_pos else 0.0))
else:
	exp_val_q = abs(pos -curr_pos)
	if exp_val_q%2!=qcount%2 or qcount<exp_val_q:
		print("{:.12f}".format(0.0))
	else:
		neg = (qcount - exp_val_q)/2
		posi = qcount - neg
		val = factorial(qcount)/(factorial(neg)*factorial(posi)*pow(2,qcount))
		print("{:.12f}".format(val))



