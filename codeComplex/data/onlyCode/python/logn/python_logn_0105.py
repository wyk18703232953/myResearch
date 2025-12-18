l,r=map(int,input().split())
if(l==r):
    print(0)
else:
    if(r&(r-1)==0):
        print(r^(r-1))
    else:
        x=l^r
        p1=1
        while(p1<=x):
            p1*=2
        print(p1-1)
  	   		      	  	 	 	    			 	