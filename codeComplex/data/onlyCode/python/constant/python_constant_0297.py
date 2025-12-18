from sys import stdin,stdout
from math import ceil
nmbr = lambda: int(stdin.readline())
lst = lambda: list(map(int, stdin.readline().split()))
for _ in range(1):#nmbr()):
    k,n,s,p=lst()
    spp=ceil(n/s)
    tots=spp*k
    print(ceil(tots/p))
									 	 	 	  	   	    		 		