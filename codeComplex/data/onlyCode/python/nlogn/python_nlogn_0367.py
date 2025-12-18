n , k = map(int, input().split())
l = list(map(int,input().split()))
l.sort()
a = 0
i = 0
while i<(n-1):
    j = i+1
    while j<n and l[j]==l[i]:
        j+=1
    if j==n:
        break
    else:
        if l[j]<=l[i]+k:
            a+=(j-i)
    i = j
print(n-a)