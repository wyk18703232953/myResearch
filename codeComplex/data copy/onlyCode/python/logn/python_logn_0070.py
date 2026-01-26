import math

l1 = input().split()
#l2 = input().split()

l1 = [int(i) for i in l1]

l2 = l1[1]
l1 = l1[0]

#l2 = [[int(i)] for i in l2]
#l2 = [0] + l2

x=l1^l2;
y=1;
while(y<=x):
  y=y*2;

print(y-1);

  	   	  	    	  			   				  		