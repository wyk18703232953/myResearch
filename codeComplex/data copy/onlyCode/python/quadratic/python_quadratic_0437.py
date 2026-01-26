
_=input()
n=input()
num=int(n)

list_n=list(n)
list_n_int=list(map(int,n))


lower=max(list_n_int)
total=sum(list_n_int)
upper=int(total/2)

flag=False
if lower == 0:
    print("YES")
else:
    for i in range(lower,upper+1):
        flag=True
        p=0
        temp=0
        each=i
        seg=total/each
        if seg.is_integer():
            while p < len(n):

                temp+=list_n_int[p]
                if temp < each:
                    p+=1
                elif temp == each:
                    temp=0
                    p+=1
                else:
                    flag=False
                    break
            if flag:
                print("YES")
                break
        else:
            flag=False
    if not flag:
        print("NO")
