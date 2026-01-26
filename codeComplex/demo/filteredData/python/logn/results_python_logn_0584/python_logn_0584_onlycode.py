import math

def solutions(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    if sol1<0 and sol2>0:
        return sol2
    elif sol1>0 and sol2<0:
        return sol1
    else:
        return 0
    
    
    

x = input()
x=x.split(" ")
c = int(x[0])
m = int(x[1])

print(int(c-solutions(1,3,-(2*c+2*m))))

				  	 	 	  	   	    			  				