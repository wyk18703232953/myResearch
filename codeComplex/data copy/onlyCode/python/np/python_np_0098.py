import  math
s=str(input())
s2=str(input())
p,m,res,ans,temp,i=0,0,0,0,0,0
p=s.count("+")
m=s.count("-")
q=s2.count("+")
w=s2.count("-")
pr,mr=p-q,m-w
if pr <0 or mr<0:
    print("%.12f"%0)
else:
    temp=pr+mr
    if temp==0:
        print('%.12f'%1)
    else:
        i=pow(2,temp)
        res=math.factorial(temp)/(math.factorial(pr)*math.factorial(mr))
        ans=res/i
        print("%.12f"%ans)
