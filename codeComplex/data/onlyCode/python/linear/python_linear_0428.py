test=int(input())
first=[]
for i in range(test):
    list_=list(map(int,input().split()))
    sum_=sum(list_)
    first.append(sum_)
first_sum=first[0]
count=0
for i in first:
    if first_sum<i:
        count=count+1 
    else:
        continue
print(count+1)