import math
import sys

def minPut(n):
    return math.ceil((-1 + math.sqrt(1-4*(-n*2))) / 2)
def nCandies(n):
    return int(n*(n+1)/2)

actions, candies = map(int, sys.stdin.readline().split())

put = minPut(candies)
putCandies = nCandies(put)

eat = putCandies - candies

while put + eat < actions:
    eat += put + 1
    put += 1
    
print(eat)