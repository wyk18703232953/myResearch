n = int(input())

if(n>=0):
    print(n)
    exit()
else:
    n=str(abs(n))
    n1=int(n[:len(n)-1])

    temp=n[len(n)-1]

    n2=n[:len(n)-2]

    n2=int(n2+temp)
    #print(n2)

if(n1<=n2):
    if(n1!=0):
        print('-'+str(n1))
    else:
        print(0)
else:
    if(n2!=0):
        print('-'+str(n2))
    else:
        print(0)