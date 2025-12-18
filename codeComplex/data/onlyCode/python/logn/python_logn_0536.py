k=int(input(''))
a=[9]
i=1
if k<10:
    print(k)
else:
    while k>a[-1]:
        a.append((10**(i+1)-10**(i))*(i+1)+a[i-1])
        i+=1
    #print(a)
    cat=len(a)
    diff=k-a[-2]
    step=int(diff/(cat))
    rem=diff%(cat)
    #print('category={}'.format(cat))
    #print('difference={}'.format(diff))
    #print('step ={}'.format(step))
    #print('remainder ={}'.format(rem))
    if rem==0:
        number=(10**(cat-1)-1)+step
     #   print(number)
        print(str(number)[-1])
    else:
        number=10**(cat-1)+step
       # print(number)
        print(str(number)[rem-1])