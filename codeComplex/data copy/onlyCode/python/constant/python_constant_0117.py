n=int(input())
if n >= 0:
 
    print(n)
 
else:
 
    a = int(n / 10)
    b=int(n/100)*10 - abs(n)%10
    
    print(max(a,b))