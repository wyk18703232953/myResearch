import sys
input = sys.stdin.readline

'''

'''

n = int(input())
a = list(map(int, input().split()))
swaps = 0
for i in range(0, 2*n, 2):
    if a[i] == a[i+1]:
        continue
    
    c = a[i]
    j = i + 2
    while c != a[j]:
        j += 1
    
    MIN = i+1
    while j > MIN:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1
        swaps += 1

print(swaps)
