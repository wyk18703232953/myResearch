def iskoutsu(arr):
	return len(set(arr)) == 1

def isshuntsu(arr):
	nos = [int(ele[0]) for ele in arr]
	nos.sort()
	return nos[0]+1 == nos[1] and nos[1]+1 == nos[2] and len(set([ele[1] for ele in arr])) == 1

arr = input().strip().split()
if isshuntsu(arr) or iskoutsu(arr):
	exit(print(0))

# to make koutsu
total1 = 0
if len(set(arr)) == 3:
	total1 = 2
elif len(set(arr)) == 2:
	total1 = 1

# to make shuntsu
total2 = 2
for ele in arr:
	no, suite = int(ele[0]), ele[1]
	
	if no+2 <= 9:
		required = [str(no+1)+suite, str(no+2)+suite]
		curr = int(required[0] not in arr) + (required[1] not in arr)
		total2 = min(total2, curr)

	if no+1 <= 9 and no-1 >= 0:
		required = [str(no-1)+suite, str(no+1)+suite]
		curr = int(required[0] not in arr) + (required[1] not in arr)
		total2 = min(total2, curr)

	if no+2 <= 9:
		required = [str(no-1)+suite, str(no-2)+suite]
		curr = int(required[0] not in arr) + (required[1] not in arr)
		total2 = min(total2, curr)

print(min(total1, total2))