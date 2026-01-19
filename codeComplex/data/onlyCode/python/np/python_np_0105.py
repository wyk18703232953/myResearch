import math

def find_nCr(n, r):
	return (math.factorial(n) / (math.factorial(r)*math.factorial(n-r)) )

sent = input()
received = input()

final_pos = 0
current_pos = 0
uncertain = 0

for s in sent:
	if s == "+":
		final_pos += 1
	else:
		final_pos -= 1

for s in received:
	if s == "+":
		current_pos += 1
	elif s == "-":
		current_pos -= 1
	else:
		uncertain += 1

if uncertain == 0:
	if final_pos == current_pos:
		print(1)
	else:
		print(0)
else:
	# the uncertain ones can be all plus or all minus or mixture of plus/minus
	# for all plus we go current_pos+uncertain
	# then for each minus (current_pos+uncertain) decreases by 2
	# so positions is a list of all the posible positions we can go
	positions = list(range(current_pos-uncertain, current_pos+uncertain+2, 2))
	
	# print(positions)

	try:
		pos_index = positions.index(final_pos)
		a = find_nCr(uncertain, pos_index)
		b = math.pow(2, uncertain)
		print(a/b)
	except:
		pos_index = -1
		print(0)
