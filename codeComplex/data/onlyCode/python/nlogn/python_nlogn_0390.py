import sys
import heapq

n, k = list(map(int,sys.stdin.readline().strip().split(' ')))
p = list(map(int,sys.stdin.readline().strip().split(' ')))
c = list(map(int,sys.stdin.readline().strip().split(' ')))

sortedp = sorted([(pi,i) for (i,pi) in enumerate(p)])

ans = [0 for i in range(n)]
acc_coins = 0
acc = []

if k == 0:
	print(' '.join(map(str,c)))
else:
	for i in range(n):
		coins = c[sortedp[i][1]]
		ans[sortedp[i][1]] += acc_coins + coins
		if len(acc) < k:
			acc_coins += coins
			heapq.heappush(acc,coins)
		else:
			smallest_coin = heapq.nsmallest(1,acc)[0]
			if smallest_coin < coins:
				acc_coins -= smallest_coin
				heapq.heappop(acc)
				heapq.heappush(acc,coins)
				acc_coins += coins
	print(' '.join(map(str,ans)))
