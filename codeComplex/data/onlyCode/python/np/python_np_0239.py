#_______________________________________________________________#
def fact(x):
	if x == 0:
		return 1
	else:
		return x * fact(x-1)
def lower_bound(li, num): 
	answer = -1
	start = 0
	end = len(li)-1

	while(start <= end):
		middle = (end+start)//2
		if li[middle] >= num:
			answer = middle
			end = middle - 1
		else:
			start = middle + 1
	return answer #index where x is not less than num
def upper_bound(li, num): 
	answer = -1
	start = 0
	end = len(li)-1

	while(start <= end):
		middle = (end+start)//2

		if li[middle] <= num:
			answer = middle
			start = middle + 1
		
		else:
			end = middle - 1
	return answer #index where x is not greater than num

def abs(x):
	return x if x >=0 else -x
def binary_search(li, val, lb, ub): 
	ans = 0
	while(lb <= ub):
		mid = (lb+ub)//2
		#print(mid, li[mid])
		if li[mid] > val:
			ub = mid-1
		elif val > li[mid]:
			lb = mid + 1
		else:
			ans = 1
			break
	return ans
def kadane(x): #maximum sum contiguous subarray
	sum_so_far = 0
	current_sum = 0
	for i in x:
		current_sum += i
		if current_sum < 0:
			current_sum = 0
		else:
			sum_so_far = mpos(sum_so_far,current_sum)
	return sum_so_far
def pref(li):
	pref_sum = [0]
	for i in li:
		pref_sum.append(pref_sum[-1] + i)
	return pref_sum
def graph(n,m):
	adj = dict()
	for i in range(1,n+1):
		adj.setdefault(i,0)
	for i in range(m):
		a,b = map(int,input().split())
		adj[a] += 1
		adj[b] += 1
	return adj

#_______________________________________________________________#
'''
      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ▄███████▀▀▀▀▀▀███████▄
░▐████▀▒▒Aestroix▒▒▀██████
░███▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀████
░▐██▒▒▒▒▒KARMANYA▒▒▒▒▒▒████▌         ________________
░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌  ? ?   |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|
░░█▒▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▒▐███▌   ?    |___CM ONE DAY___|
░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▒▐███▌     ? ? |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|
░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌    ? ?    
░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌      ? 
░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█     ? ? 
░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀       ? 
░░░░▄█████████ ████=========█▒▒▐▌
░░░▀███▀▀████▀█████▀▒▌
░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐
░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐
░░░░░████████████████
'''
import sys
import threading
from math import *
#sys.setrecursionlimit(900000)
#threading.stack_size(10**5)  # remember it cause mle
#def main():
#for _ in range(int(input())):
for _ in range(1):
	#n = int(input())
	n,l,r,x = map(int,input().split())
	#n, s = input().split()
	#s = list(input())
	#a = [int(x) for x in s]
	#s = list(input())
	a = list(map(int,input().split()))
	#b = list(map(int,input().split()))
	#adj = graph(n,m)
	
	cnt = 0
	for mask in range(1,(1<<n)+1):
		mini = 10**9 + 10
		maxi = 0
		elem = 0
		sumi = 0
		for j in range(n):
			if mask & (1<<j): #if the bitmask array element is 1
				elem += 1
				sumi += a[j]
				mini = min(mini, a[j])
				maxi = max(maxi, a[j])
		#print(elem,sumi,maxi,mini,bin(mask))
		if elem >= 2:
			if (l <= sumi <= r) and (maxi-mini >= x):
				cnt += 1
	print(cnt)



















































'''		
t = threading.Thread(target=main)
t.start()
t.join()
'''









	




