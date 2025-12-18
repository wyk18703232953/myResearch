# import sys 
# sys.stdin = open('input.txt', 'r')  
# sys.stdout = open('output.txt', 'w')

a = [int(i) for i in list(input())]
b = [int(i) for i in list(input())]

if (len(a)<len(b)):
	a.sort(reverse=True)
	ans = 0
	for i in range(len(a)):
		ans = ans*10+a[i]
	print(ans)
else:
	# ans = [0]*len(a)
	ans = 0
	n = len(a)
	count = [0]*10
	for i in range(n):
		count[a[i]] += 1
	i = 0
	while (i<n):
		x = b[i]
		if (count[x]>0):
			ans = ans*10+x
			count[x] -= 1
			i += 1
		else:
			break
	if (i==n):
		print(ans)
		exit(0)
	x = b[i]
	flag = False
	for j in range(x-1,-1,-1):
		if (count[j]>0):
			ans = ans*10+j
			count[j] -= 1
			flag = True
			break
	if (flag) :
		for j in range(9,-1,-1):
			while (count[j]>0):
				ans = ans*10+j
				count[j] -= 1
	else:
		while (not flag):
			t = ans%10
			ans = ans//10
			count[t] += 1
			for i in range(t-1,-1,-1):
				if (count[i]>0):
					count[i] -= 1
					flag = True
					ans = ans*10 + i
					break
		for j in range(9,-1,-1):
			while (count[j]>0):
				ans = ans*10+j
				count[j] -= 1
	print(ans)
