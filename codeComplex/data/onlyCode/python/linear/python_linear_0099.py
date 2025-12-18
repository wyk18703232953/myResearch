n = int(input())
s = input()
want = len(set(s))
d = {}
j = 0
count = 0
ans = float("inf")
for i in range(n):
    if s[i] not in d:
        d[s[i]] = 0
        count+=1
    d[s[i]]+=1
    if count==want:
        while d[s[j]]>1:
            d[s[j]]-=1
            j+=1
        ans = min(ans,i-j+1)
print(ans)