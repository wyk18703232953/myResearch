#if boz contains at least 1 candy : take candy out and eat it
# candy in box -=1
#put candies:  if 2 times this chouse then se le suma 1
#the first move is to always put candy in the box
# n = numbers of moves
# k numbers of candies
#x(x+1)/2 - (n-x) =k
#x(x+1)/2
import math
def sportMafia(n,k):
    r=round(n+1.5-math.sqrt(2*(n+k)+2.75))
    return r
    #ini=-1
    #fin=n+1
    #while (fin-ini)>1:
     #   mid=(ini+fin)/2
      #  x=n-mid
        #x(x+1)/2 - n-x
       # if ((x*(x-1)/2)- mid)>k:
        #  ini=mid;
        ##else:
         #   fin=mid
        #return fin
    #return 0

        
        
    

n,k = map(int,input().split())
print(sportMafia(n,k))

				  	   	   	  		 	   					 	