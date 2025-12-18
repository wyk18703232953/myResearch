mass = list(input())
b = int(input())
mass.sort()
mass = mass[::-1]
p = ''
while(len(mass)>0):
	for i in range(len(mass)):
		n = p + mass[i] + ''.join(sorted(mass[:i] + mass[i + 1:]))
		if int(n) <= b:
			p += mass[i]
			mass = mass[:i] + mass[i + 1:]
			break
print(p)