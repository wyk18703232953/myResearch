n=int(input())
lst = list(map(int, input().strip().split(' ')))
c=0
while(len(lst)!=0):
    p=lst[0]
    del lst[0]
    i=lst.index(p)
    c+=i
    del lst[i]
print(c)
    