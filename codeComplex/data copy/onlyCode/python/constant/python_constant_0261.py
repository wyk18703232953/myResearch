n,pos,l,r = map(int, input().split())
dl,dr = abs(pos-l) + 1, abs(pos-r) + 1
print(dr*(r<n) if l==1 else dl if r==n else min(dl,dr)+r-l+1)