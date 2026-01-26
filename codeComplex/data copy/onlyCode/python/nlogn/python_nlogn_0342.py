o=int(input())
uk=[]
gh=0
uo=0
for i in range(o):
    yu=input()
    if(len(yu)>gh):
        gh=len(yu)
        uo=i
    uk.append(yu)
        
yk=0
yj={}

td=0  
uk.sort()
for i in range(len(uk)-1):
    for j in range(i+1,len(uk)):
        if(len(uk[j])<len(uk[i])):
            t=uk[j]
            uk[j]=uk[i]
            uk[i]=t
for i in range(1,len(uk)):
    j=i
    while(j>=0):
        if(uk[i].count(uk[j])==0):
            td=1
        j=j-1
if(td==0):        
    print('YES')   
    for i in uk:
        print(i)            
else:   
    print('NO')

 		 	 			 					 						     		