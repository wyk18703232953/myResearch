import math
n = int(input())

if n>0:
    print(n)
else:
    l = list(str(n))
    
    last = l[0:len(l)-1]
    second = l[0:len(l)-2]
    second+=l[-1]
    lR = "".join(last)
    sR = "".join(second)
    
    
    
    print(max(eval(lR),eval(sR)))

        
    
    




    
    
            


   