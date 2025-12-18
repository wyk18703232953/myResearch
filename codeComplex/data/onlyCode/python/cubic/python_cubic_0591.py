a=input()
b=input()

if len(b)>len(a):

    l=[int(i) for i in a]
    l.sort()
    l=l[::-1]
    temp=[str(i) for i in l]
    s=''.join(temp)
    print(s)

else:
    d={}

    for i in a:

        if i not in d:

            d[i]=1
        else:

            d[i]=d[i]+1

  

    def find(i):

        global flag
        if i in d and d[i]>0:

            d[i]=d[i]-1

            return(i)

        for j in range(int(i),-1,-1):

            flag=1

            j=str(j)
            
            if j in d and d[j]>0:

                d[j]=d[j]-1

                return(j)

    def fun(d):

        l=[]
        for i in d:

            if d[i]>0:

                
                l=l+[int(i)]*d[i]
        l.sort()
        l=l[::-1]
        temp=[str(i) for i in l]

        s=''.join(temp)

        return(s)


    def fun2(x):

        global new
        for i in range(x-1,-1,-1):
            
            temp=new[i]
            for j in range(int(temp)-1,-1,-1):

                j=str(j)
                
                if j in d and d[j]>0:

                    new=new[:i]+str(j)
                    d[j]=d[j]-1

                    d[temp]=d[temp]+1

                    return(new)
                
            d[temp]=d[temp]+1

                    

                    

                    
                

            
        

    flag=0
    new=''
    for i in range(len(b)):
        
        if flag==0:

            temp=find(b[i])
            
            if temp==None:
              
                new=fun2(i)
           
                
                new=new+fun(d)

                break


                    

                

            else:
                new=new+temp
            
        else:

            new=new+fun(d)
            break
       

            
    print(new)

