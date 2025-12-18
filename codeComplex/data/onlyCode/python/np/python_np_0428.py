# based on solution by @conqueror_of_tourist
import sys

reader = (map(int, line.split()) for line in sys.stdin)
input = reader.__next__

n, m = input()
arrays = []
for i in range(n):
    arrays.append(list(input()))

full = (1 << m) - 1
L = -1
R = 10 ** 9 + 1
while L + 1 < R:
    check = (L + R) >> 1
    
    masks = {}
    for i, arr in enumerate(arrays):
        curr = 0
        for val in arr:
            curr <<= 1
            if val >= check:
                curr |= 1
        masks[curr] = i
    
    isValid = False
    for k1 in masks:
        for k2 in masks:
            if k1 | k2 == full:
                ans0 = masks[k1]
                ans1 = masks[k2]
                isValid = True
                break
        if isValid:
            break
    
    if isValid:
        L = check
    else:
        R = check

print(ans0 + 1, ans1 + 1)
