def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
n=int(input());d=0
if n%2==0:
    print('4 '+str(n-4))
else:
    i=4
    while i<=int(n//2)+1:
        k=n-i
        if isPrime(k)==False:
            print(str(i)+' '+str(k))
            break
        i+=2

            
        
            
