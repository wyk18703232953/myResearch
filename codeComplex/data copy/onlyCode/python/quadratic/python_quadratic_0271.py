n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

print(*sorted([x for x in arr2 if x in arr1],key = lambda k:arr1.index(k)))