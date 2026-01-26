n=int(input())
def judge(x):
    if x%2==0:
        return 0
    else:
        return 1
ls=[int(x) for x in input().split()]
if judge(ls[0])==judge(ls[1]):
    for x in ls[2:]:
        if judge(x)!=judge(ls[0]):
            print(ls.index(x)+1)
            break
else:
    if judge(ls[2])==judge(ls[0]):
        print(2)
    elif judge(ls[2])==judge(ls[1]):
        print(1)