n = int(input())
lst = list(map(int,input().split()))
lst = set(lst)
lst = list(lst)
lst.remove(min(lst))
if(len(lst)==0):
    print("NO")
else:
    print(min(lst))
    		 		 						 	 	     	    	