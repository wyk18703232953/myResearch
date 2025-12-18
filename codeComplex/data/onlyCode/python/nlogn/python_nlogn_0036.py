def replace(arr):
    if arr==[1]*len(arr):
        arr[-1]=2
        print(*sorted(arr))
        return ""
    arr[arr.index(max(arr))]=1
    print(*sorted(arr))
    return ""
a=input()
lst=list(map(int,input().strip().split()))
print(replace(lst))