s = input()

mc = -1

for i in range(len(s)):
	for j in range(i+1, len(s)):
		cu = 0
		for cu in range(len(s)-max(i, j)):
			if s[i+cu] == s[j+cu]:
				mc = max(mc, cu)
			else:
				break
		

print(mc + 1)
			
