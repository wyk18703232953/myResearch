a = []
n = int(input())
for _ in range(n):
    a.append(input())
if n==1:
    print("YES")
    print(a[0])
else:
    a.sort(key = len)
    for i in range(1,n):
        if a[i-1] not in a[i]:
            print("NO")
            break
    else:
        print("YES")
        for i in a:
            print(i)
        
