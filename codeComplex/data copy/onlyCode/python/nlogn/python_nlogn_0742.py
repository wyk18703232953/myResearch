n = int(input())
a = list(map(int, input().split()))
summ=0
a.sort()
if len(a)==1:
    if a[0]%2==1:
        print('sjfnb')
    else:
        print('cslnb')
elif a[0] == a[1]==0:
    print('cslnb')
else:
    x = False
    for i in range(2, n):
        if a[i]==a[i-1] and a[i-1]==a[i-2]:
            x=True
    if x:
        print('cslnb')    
    else:
        x = False
        for i in range(2, n):
            if a[i]==a[i-1] and a[i]-1==a[i-2]:
                x=True
        if x:
            print('cslnb')
        else:
            summ=0
            for i in range(1, n):
                if a[i]==a[i-1]:
                    summ+=1
            if summ>1:
                print('cslnb')
            else:
                summ=0
                for i in range(n):
                    summ+=a[i]-i
                if summ%2==0:
                    print('cslnb')
                else:
                    print('sjfnb')
        