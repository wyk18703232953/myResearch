import sys
import os.path
from collections import *
import math
import bisect

if (os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
else:
    input = sys.stdin.readline

############## Code starts here ##########################

n = int(input())

if(n == 2 or n == 3 or n == 4 or n == 5):
    print(-1)
else:
    print(1,2)
    print(2,3)
    print(2,4)
    for i in range(5,n + 1):
        print(4,i)

for i in range(2,n + 1):
    print(1,i)

############## Code ends here ############################
