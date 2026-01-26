n=int(input())
list1=list(map(int,input().split(' ')))
sum2=0
sum1=0
count=0
list1.sort(reverse=True)
for i in range(len(list1)):
    sum1=sum1+list1[i]
 
for i in range(len(list1)):
    if(int(sum1/2)>=sum2):
        sum2=sum2+list1[i]
        count=count+1
print(count)