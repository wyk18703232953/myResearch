n = int(input())
queen = list(map(int,input().split(" ")))
king = list(map(int,input().split(" ")))
target = list(map(int,input().split(" ")))

def done():
	print("NO")
	exit()

def complete():
	print("YES")
	exit()

# king is left of queen
if king[0] < queen[0]:
	if target[0] > queen[0]:
		done()
	# king is higher than queen
	if king[1] > queen[1]:
		if target[1] < queen[1]:
			done()
		complete()
	else:
		if target[1] > queen[1]:
			done()
		complete()
else:
	if target[0] < queen[0]:
		done()
	if king[1] > queen[1]:
		if target[1] < queen[1]:
			done()
		complete()
	else:
		if target[1] > queen[1]:
			done()
		complete()
	
