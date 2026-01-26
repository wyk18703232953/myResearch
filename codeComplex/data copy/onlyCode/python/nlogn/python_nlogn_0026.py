n = int(input())

l = list(map(int,input().split()))

s = list(set(l))

s.sort()

if len(s)>1:
    ans = s[1]
else:
    ans='NO'
    
print(ans)