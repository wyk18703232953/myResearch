n = int(input())
s = input()
t = input()
sl = [i for i in s]
tl = [i for i in t]
ans = []
if(''.join(sorted(s))!=''.join(sorted(t))):
    print(-1)
    
    
#birute phoerce
#i = 1 to n 
#j = i+1 to n
else:
    for i in range(n):
        if(sl[i]!=tl[i]):
            for j in range(i+1,n):
                if(sl[j]==tl[i]):
                    break
            for k in range(j-1,i-1,-1):
                sl[k],sl[k+1] = sl[k+1],sl[k]
                ans.append(k+1)
    #print(sl,t)
    print(len(ans))
    for i in ans:
        print(i,end=' ')