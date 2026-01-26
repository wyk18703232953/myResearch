def A(n):
	return (4**n-1)//3

L = 31

T = int(input())
for _ in range(T):
	n,k = [int(_) for _ in input().split()]

	if n > L:
		print("YES",n-1)
		continue

	if k > A(n):
		print("NO")
		continue

	E = 1
	M = 0
	R = 0
	while n >= 0:
		M += E

		I = 2*E-1
		E = 2*E+1

		n -= 1
		R += I*A(n)

		if M <= k and k <= M+R: break

	if n >= 0: print("YES",n)
	else: print("NO")
