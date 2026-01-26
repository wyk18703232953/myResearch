z,x=map(int,input().split())
z-=1;x-=1
if x*(x+1)/2 < z :
  print(-1)  
elif z==0:
    print(0)
elif z==x:
    print(1)    
else:
    import sys           
    start = 1 ; end = x  
    while end > start:    
        mid = (end +start)//2
        ans =(x*(x+1)//2)-((mid-1)*(mid)//2 )
        if ans == z:
            print(x-mid+1)
            sys.exit(0)  
        elif ans > z:
            start = mid+1   
        elif ans < z:
            end = mid      
    print(x-end+2)
   
