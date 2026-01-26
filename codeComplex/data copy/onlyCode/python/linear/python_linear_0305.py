import math

n = int(input())
a = list(map(lambda x : int(x), input().split()))
q = len(a)

earliest_time = pow(10, 9) + 1000
earliest_queue = 1
for i in range(q):
    n = int(max(0, math.ceil((a[i] + 1 - (i + 1)) / q)))
    t = (i + 1) + n * q
    if t < earliest_time:
        earliest_time = t
        earliest_queue = i + 1

print(earliest_queue)
