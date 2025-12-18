#digits sequence(Hard Edition)

n = int(input())

check = True
t=0
tnext=9

count=1
i=1
j=1
res = 0
while(check):
    
    if(n<=tnext):
        res=n-t
        check = False

    else:
        #sm1 = sm1+t
        count = count+1

        if(t!=0):
            t=t+9*i*j
        else:
            t=9

        tnext = tnext + 9 * (i+1)*(j*10)
        i=i+1
        j=j*10
        
num1 = int(res/count)
num2 = res%count


#print(count , t , tnext , sm1 )


des = pow(10,count-1)
despac = des + num1 


#print(despac)

if(num2 == 0):
    despac = str(despac -1)
    print(despac[-1])

else :
    despac = str(despac)
    print(despac[num2-1])
