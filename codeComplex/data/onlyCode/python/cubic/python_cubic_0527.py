from collections import defaultdict

def f(b,d):
    fi = int(b[0])
    if len(b)==1:
        j=fi
        while(j>=0):
            if d[j]:
                return str(j)
            j+=-1

        return ""


    fi=int(b[0])
    s=""
    if d[fi]>0:
        d1=defaultdict(lambda:0)
        for j in d:
            d1[j]=d[j]
        d1[fi]+=-1
        s=f(b[1:],d1)

    if s!="":
        return str(fi)+s

    else:
        s1=""
        j=fi-1
        while(j>=0):
            if d[j]>0:
                s1+=str(j)
                d[j]+=-1
                break
            j+=-1
        if s1=="":
            return ""
        else:
            j=9
            while(j>=0):
                if d[j]==0:
                    j+=-1

                else:
                    s1+=str(j)
                    d[j]+=-1

            return s1












a=input()
b=input()
d=defaultdict(lambda:0)
res=[]
for j in a:
    d[int(j)]+=1
    res.append(int(j))
res.sort(reverse=True)
for j in range(len(a)):
    res[j]=str(res[j])
if len(b)>len(a):
    print("".join(res))

else:
    print(f(b,d))

