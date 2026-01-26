n=int(input())
s=0; pred=0
for i in range(1,20):
    m=9*pow(10,i-1)*i
    s+=m    
    if n<=s:        
        nd=pow(10,i-1)              
        sme=n-pred               
        num=sme//i
        ost=sme%i
        if ost==0:
            dig=nd+num-1
        else:
            dig=nd+num       
        d=i
        rez=[]
        ddig=dig
        while d>0:
            o=ddig%10
            a=ddig//10
            rez.append(o)
            d-=1
            ddig=a        
        break
    pred=s
print(str(rez[-ost]))
