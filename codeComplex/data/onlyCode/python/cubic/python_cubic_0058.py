n=input()
m={}
def podstroka(s:str):
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] in m:
                m[s[i:j]] +=1
            else:
                m[s[i:j]] = 1
    return m        



podstroka(n)


maxlen = 0
for x in m:
    if m[x]>=2 and len(x)>maxlen:
        maxlen=len(x)  
print(maxlen)