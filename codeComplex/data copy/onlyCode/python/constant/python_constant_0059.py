n = int(input())
f0= 0
f1 = 1
li = [0,1]
for i in range(45):
	t = f1
	f1 += f0
	f0 = t
	li.append(f1)
x = []
for i in range(3):
	for i in range(len(li)-1, -1, -1):
		if li[i] <= n:
			n -= li[i]
			x.append(li[i])
			break
if n == 0:
	print(*x, sep = " ")
else:
	print("I'm too stupid to solve this problem")
