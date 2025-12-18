def check(e,value,pre):
    global maxi,count
    e[str(value)]-=1
    pre+=str(value)
    arr=[]
    for i in e:
        for j in range(e[i]):
            arr.append(i)
    arr.sort(reverse=True)
    st=''
    for i in arr:
        st+=str(i)
    alpha=int(pre+st)
    if alpha<=int(b):
        maxi=max(maxi,int(pre+st))


a=input()
b=input()
maxi=0
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
maxi=0
num=""
count=0
if len(a)<len(b):
    check(d.copy(),max(d),'')
else:
    for i in b:
        if i in d and d[i]>0:
            for j in range(int(i)-1,-1,-1):
                if str(j) in d and d[str(j)]>0:
                    check(d.copy(),j,num)
                    break
            check(d.copy(),i,num)
            num+=i
            d[i]-=1

        else:
            j=0
            for j in range(int(i)-1,-1,-1):
                if str(j) in d and d[str(j)]>0:
                    check(d.copy(),j,num)
                    break
            break
print(maxi)