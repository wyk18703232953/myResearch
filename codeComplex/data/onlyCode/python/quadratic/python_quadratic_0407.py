def prefix_func(s):
    slen, k = len(s), 0
    p = [0]*slen
    p[0] = 0
    for i in range(1, slen):
        while k>0 and s[k] != s[i]:
            k = p[k-1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p
n,k=map(int,input().split())
s=input()
l=prefix_func(s)[-1]
print(s+s[l:]*(k-1))
