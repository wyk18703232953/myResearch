num=int(input())

vals=list(map(int,input().split()))

vals.sort()

flag=0

for i in vals:
    if i>vals[0]:
        print(i)
        flag=1
        break
    

if flag==0:
    print('NO')
    