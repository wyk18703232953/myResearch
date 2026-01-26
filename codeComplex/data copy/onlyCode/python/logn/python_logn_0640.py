data=list(map(int, input().split()))
sum=0
cont=0
res=0
con2=0
con3=0
for i in range(data[0]):
    sum=sum+con2
    con2+=1
    res=data[0]-con2
 
    if data[1]==0:
        if sum>= res:
            cont+=1
            
    else:
        if sum>data[1]:
            if res+1 == sum-data[1]:
                cont=res+1
                break
print(cont)
    	  		  	   	 					  		   		