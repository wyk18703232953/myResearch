#import math
M = 10**9 + 7
R = lambda: map(int, input().split())
x,k = R()
if x == 0:
    print(0)
    quit()
print(((pow(2,k+1,M)*x)%M - pow(2,k,M) +1 ) % M)