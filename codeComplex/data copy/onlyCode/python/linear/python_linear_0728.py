import os
import sys

def log(*args, **kwargs):
    if os.environ.get('CODEFR'):
        print(*args, **kwargs)


n, k = tuple(map(int, input().split()))

s = '0'*((n-k)//2) + '1'

for i in range(n):
    print(s[i % len(s)], end='')
print()

