n,t=int(input()),1
while n>0:
        if n!=3:  
            k=n//2+n%2
            print((str(t)+' ')*k,end= '')
            n-=k
            t*=2
        else:
            print(t,t,t*3)
            n=0
