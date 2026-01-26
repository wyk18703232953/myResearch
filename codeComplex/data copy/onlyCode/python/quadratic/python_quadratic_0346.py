# RawCoder : https://bit.ly/RCyouTube
# Author : MehulYK

n = int(input())
s = list(input())
d = list(input())
if(sorted(s) != sorted(d)):
    print(-1)
else:
    ans = []
    for i in range(n):
        if(s[i] != d[i]):
            for u in range(i+1,n):
                if(s[u] == d[i]):
                    ind = u
                    break
                    
            cnt = abs(ind - i)
            s.pop(ind)           
            s.insert(i,d[i])
            #print(s)
            for k in range(cnt):
                if(ind > 0):
                    ans.append(ind)
                else:
                    ans.append(1)    
                ind -= 1
    print(len(ans))
    print(*ans)