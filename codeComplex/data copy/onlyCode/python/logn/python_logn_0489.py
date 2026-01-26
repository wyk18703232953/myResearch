import math
k = int(input())

flag = True
i = 0
value=0

if(k <= 9):
    print(k)

else:
    while(flag):
        a = 9 * pow(10, i) * (i+1)
        if(k >= a):
            k -= a
            value+=9 * pow(10, i)
            i+=1
        else:
            n=int(math.ceil(k/(i+1)))
            value+=n
            index=k%(i+1)-1
            print(str(value)[index])
            flag=False
    


        
