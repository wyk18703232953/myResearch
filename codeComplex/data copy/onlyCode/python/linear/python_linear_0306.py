n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = (arr[i]-i)//n + (1 if (arr[i]-i)%n>0 else 0)
print(arr.index(min(arr))+1)
