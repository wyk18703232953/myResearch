
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

arr.sort(key=lambda x: len(x))
flag=False
for i in range(n-2,-1,-1):
    if arr[i] not in arr[i+1]:
        flag=True
        break

if flag:
    print("NO")
else:
    print("YES")
    for i in arr:
        print(i)