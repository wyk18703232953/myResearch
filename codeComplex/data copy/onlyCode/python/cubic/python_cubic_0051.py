s=input()
for ln in range(len(s),0,-1):
    for L in range(len(s)-ln+1):
        if s[L:L+ln] in s[L+1:]:
            print(ln)
            exit()
print(0)
        
