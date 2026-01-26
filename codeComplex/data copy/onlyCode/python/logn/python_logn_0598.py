n,a=list(map(int,raw_input().split()))
deb=1
fin=n+1
while fin-deb>1:
    m=(fin+deb)//2
    if (m*(m+1))//2-(n-m)>a:
        fin=m
    else:
        deb=m                
print(n-deb)
