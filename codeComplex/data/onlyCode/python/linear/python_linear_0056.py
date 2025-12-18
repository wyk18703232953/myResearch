num=int(input())

a=input()

b=input()

dic={}

lis=[]

ham=0

swap1=-1

swap2=-1

p=False

q=False

for i in range(num):

    if a[i]!=b[i]:

        ham+=1

        lis.append(i)

        dic[b[i]]=i

for i in lis:

    if a[i] in dic:

        p=True

        swap1=i+1

        f=dic[a[i]]

        swap2=f+1

        if a[f]==b[i]:

            q=True

            break

print(ham-(2 if q else 1 if p else 0))

print(swap1,swap2)



# Made By Mostafa_Khaled