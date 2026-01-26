x=input();l=len(x);m=0
for i in range(l-1):
    f=i
    while 1 : 
        idx = x[f+1:].find(x[f])         
        if idx == -1 :
            break
        else:
            idx += f+1 ; c=ans=0
            for j in range(idx , l) :
               if x[j] == x[i+c]:
                    ans+=1
                    c+=1  
               else:
                   break
               
            if m < ans :
                m=ans
            f = idx              
print(m)

 				         			 	 						   		