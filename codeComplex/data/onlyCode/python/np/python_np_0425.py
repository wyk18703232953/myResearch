#!/usr/bin/env python3
import sys
input = sys.stdin.readline
 
max_val = 0
n, m = [int(item) for item in input().split()]
array = []
for i in range(n):
    line = [int(item) for item in input().split()]
    array.append(line)
    max_val = max(max_val, max(line))
 
good = (1 << m) - 1
l = 0; r = max_val + 1
a = 0; b = 0
while r - l > 1:
    mid = (l + r) // 2
    bit_array = dict() 
    for k, line in enumerate(array):
        val = 0
        for i, item in enumerate(line):
            if item >= mid:
                val |= 1 << i
        bit_array[val] = k
    ok = False
    for key1 in bit_array.keys():
        for key2 in bit_array.keys():
            if key1 | key2 == good:
                ok = True
                i = bit_array[key1]
                j = bit_array[key2]
                break
    if ok:
        a = i; b = j
        l = mid
    else:
        r = mid
print(a+1, b+1)