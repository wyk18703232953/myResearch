import sys
import math
#import random
#sys.setrecursionlimit(100000000)
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

n,k=invr()

ans=0
lo=0
hi=n

def possible(a,b):
	koyta=a*(a+1)//2
	return koyta>=b+k

while hi>=lo:
	mid=(hi+lo)//2
	
	if possible(n-mid,mid):
		lo=mid+1
		ans=mid
	else:
		hi=mid-1

print(ans)

