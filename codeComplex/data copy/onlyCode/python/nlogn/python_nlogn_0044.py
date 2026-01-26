n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if arr[-1] == 1:
    arr[-1] = 2
else:
    arr[-1] = 1
arr.sort()
print(*arr)
