n = int(input("")) 
if n==1 or n==2: 
    print(n) 
elif n&1: 
    print((n)*(n-1)*(n-2))
else:
    if n%3==0:
        print((n-2)*(n-1)*(n-3))
    else :
         print(max(n*(n-1)*(n-3), (n-1)*(n-2)*(n-3),(n*(n-1)*(n-2))/2))