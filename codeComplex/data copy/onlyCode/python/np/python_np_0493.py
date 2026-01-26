import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

N, M, K = map(int, input().split())
P = []
D_P = {}

for i in range(N):
	S = input()
	P.append(S)
	D_P[S] = i

adj = [[] for _ in range(N)]
indeg = [0] * N

for _ in range(M):
	S, mt = input().split()
	mt = int(mt)-1

	fp = P[mt]

	if any(fp[i] not in (S[i], '_') for i in range(K)):
		print('NO')
		raise SystemExit

	for bs in range(1<<K):
		pat = ''.join(S[i] if bs & (1<<i) == 0 else '_' for i in range(K))
		if pat == fp: continue
		if pat in D_P:
			j = D_P[pat]
			indeg[j] += 1
			adj[mt].append(j)

Q = [i for i in range(N) if indeg[i] == 0]
for i in Q:
	for j in adj[i]:
		indeg[j] -= 1
		if indeg[j] == 0:
			Q.append(j)

if len(Q) == N:
	print('YES')
	print(' '.join(str(v+1) for v in Q))
else:
	print('NO')
