k1,k2,k3 = map(int, input().strip().split(' '))
l=[k1,k2,k3]
if min(k1,k2,k3)==1:
    print('yes')
elif l.count(2)>=2:
    print('yes')
elif l.count(3)==3:
    print('yes')
elif l.count(4)==2 and l.count(2)==1:
    print('yes')
else:
    print('no')