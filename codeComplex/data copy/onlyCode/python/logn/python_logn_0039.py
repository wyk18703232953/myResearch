a, b = map(int, input().split(" "))

a, b = min(a, b), max(a, b)

bina = str(bin(a))[2:]
binb = str(bin(b))[2:]

lena = len(bina)
lenb = len(binb)

ans = 0
if lena != lenb:
	ans = 2**lenb-1
else:
	a = '0'*(lena-lenb) + bina
	for i in range(lenb):
		if (bool(int(bina[i])) != bool(int(binb[i]))):
			ans = 2**(lenb-i) - 1
			break
	
		
print(ans)