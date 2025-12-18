def check(s,a):
    st=''
    for i in range(len(s)):
        st+=s[i]
    st=int(st)
    if (st>a):
        return False
    else:
        return True
a = input()
b = input()
s=[]
ans=''
for i in range(len(a)):
    s.append(a[i])
s.sort()
if (len(b)>len(a)):
    for i in range(len(s)):
        print(s[len(s)-i-1],end='')
else:
    for i in range(len(a)):
        j=0
        temp2=-1
        while ((j<len(s)-1) and (s[j+1]<=b[i])):
            j+=1
            if (s[j]!=s[j-1]):
                temp2=j-1    
        temp=s[j]
        s.remove(s[j])
        if (i==len(a)-1 or check(s,int(b[i+1:len(b)])) or temp<b[i]):
            ans+=temp
            if (ans[i]<b[i]):
                for k in range(len(s)):
                    ans+=s[len(s)-k-1]
        else:
            s.append(temp)
            s.sort()
            temp2=s[temp2]
            ans+=temp2
            s.remove(temp2)
            for k in range(len(s)):
                    ans+=s[len(s)-k-1]      
        if (len(ans)==len(a)):
            break          
print(ans)        
            
    
