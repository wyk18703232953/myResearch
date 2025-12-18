import sys


n, k = [int(i) for i in sys.stdin.readline().split()]


left = 0
right = n - 1

while left <=  right:
    mid = left + (right - left)//2
    fmid = (mid+1)*(mid +2)/2  - (n  - (mid + 1))
    if fmid == k:

        print(n - 1 - mid )
    if fmid > k:
        right = mid - 1
    else: # less or equal
        left = mid + 1






