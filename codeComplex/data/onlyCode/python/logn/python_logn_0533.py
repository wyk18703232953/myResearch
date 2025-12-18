a,b,c,d,e,f,g,h,i,j,k,l= [9*1, 90*2, 900*3, 9000*4, 90000*5, 900000*6, 9000000*7, 90000000*8, 900000000*9, 9000000000*10, 90000000000*11, 900000000000*12]
a=a; b= a+b; c= b+c; d=c+d; e=d+e; f= e+f; g= f+g; h=g+h; i=h+i; j= i+j
k= j+k; l= k+l
li1=[0,a,b,c,d,e,f,g,h,i,j,k,l]
n= int(input()); nn=0
for ii in range(1,12):
    if li1[ii-1]<n and li1[ii+1]>n:
        nn= ii
        
n= n-li1[nn-1]
r1= 10**(nn-1)
n1= n//nn
r1+= n1-1
n2= n-(n1*nn)
if n2==0:
    print(str(r1)[-1])
else:
    #print(r1, n2-1)
    print(str(r1+1)[n2-1])