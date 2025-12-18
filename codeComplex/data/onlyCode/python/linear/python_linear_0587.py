n, q = map(int, raw_input().split())
l = raw_input()
cnt1, cnt0 = [0]*(n+1), [0]*(n+1)
mod = 10**9 + 7
for i in range(len(l)):
	if l[i] == '1':
		cnt1[i+1] = cnt1[i] + 1
		cnt0[i+1] = cnt0[i]
	else:
		cnt0[i+1] = cnt0[i] + 1
		cnt1[i+1] = cnt1[i]
pow2 = [1]
for i in range(1, 10**5 + 10):
	pow2.append((2*pow2[-1])%mod)
for i in range(q):
	l, r = map(int, raw_input().split())
	ones = cnt1[r] - cnt1[l-1]
	zeroes = cnt0[r] - cnt0[l-1]
	t1 = (pow2[ones] - 1)%mod
	t2 = (((pow2[ones] - 1)%mod)*(pow2[zeroes] - 1))%mod
	print((t1+t2)%mod)