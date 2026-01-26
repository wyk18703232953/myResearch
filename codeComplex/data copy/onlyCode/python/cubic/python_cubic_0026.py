s = input()
res = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        for f in range(i+1,len(s)):
            if len(s) >= f + j-i:
                if (s[i:j]== s[f:f+j-i]):
                    res = max(res,j - i)
                    
print(res)