'''input
5 25 35 10
10 10 20 10 20
'''
from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict
from bisect import bisect_left



def check(temp):
	if len(temp) < 2:
		return False
	else:
		s = sum(temp)
		if s >= l and s <= r:
			if temp[-1] - temp[0] >= x:
				return True
			else:
				return False
		else:
			return False
 
def brute(index, temp):
	global count

	if index == n:
		if check(temp):
			count += 1

	else:
		temp.append(arr[index])
		brute(index + 1, temp)
		temp.pop()
		brute(index + 1, temp)


# main starts
n, l, r, x = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
arr.sort()
count = 0
temp = []
brute(0, temp)
print(count)
	    							    			 			   		 	