a, b = sorted(input()), int(input())
for i in range(len(a)):
	for j in range(i+1, len(a)):
		c = int(str.join('', a))
		a[i], a[j] = a[j], a[i]
		d = int(str.join('', a))
		if c <= d <= b:
		    continue
		else:
		    a[i], a[j] = a[j], a[i]
print(str.join('', a))