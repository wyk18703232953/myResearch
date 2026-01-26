from math import ceil
def test(f):
    for i in range(n):
        if (r1+ f) > f * lift[i]:
            return 0
        f -= (r1 + f) / lift[i]
        if (r1+ f) > f * land[i + 1]:
            return 0
        f -= (r1 + f) / land[i + 1]
    return 1
p=int(input())
total_wgt=int(input());r1=total_wgt
lift=list(map(int,input().split()))
land=list(map(int,input().split()));n=len(land);ans=1e20
lift+=[lift[0]];land+=[land[0]]
l=0.0;r=1e20
for i in range(1000):
  mid=(l+r)/2.0
  #print(mid)
  if test(mid):r=mid
  else:l=mid
if r<1e19:
    print('%.17f' %r)
else:
    print(-1)
