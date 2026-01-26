n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

j = 0
for i in range(n):
    if j<m and arr2[j]>=arr1[i]:
        j+=1
print(j)
