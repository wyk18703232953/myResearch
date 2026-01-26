s=list(input())
ans=0
far=0
for i in range(len(s)-1):
    if(s[i]!=s[i+1]):
        far+=1
        continue
    if(s[0]!=s[-1]):
        s[:i+1]=s[:i+1][::-1]
        s[i+1:]=s[i+1:][::-1]
        far+=1
    else:
        ans=max(ans,far+1)
        far=0
    #print(s)
print(max(far+1,ans))
# b w w w b w w b w
