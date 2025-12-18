num=int(input())
list_=sorted(set(map(int,input().split())))
if len(list_)==1:
    print("NO")
else:
    
    print(list_[1])
