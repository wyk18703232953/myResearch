k1,k2,k3=map(int,input().split())
fl=0
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            flak=1
            for i in range(8):
                if (i-i1)%k1==0 or (i-i2)%k2==0 or (i-i3)%k3==0:
                    continue
                else:
                    flak=0
            if flak==1:
                fl=1
if fl==1:
    print("YES")
else:
    print("NO")