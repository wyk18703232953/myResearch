arr = [int(i) for i in filter(None, input().split(" "))]
k_hodov = arr[0]
konf = arr[1]
left = 0
right = k_hodov+100
while(right-left)>1:
    mid = (right+left)//2
    k_give=k_hodov-mid
    if ((k_give+1)*(k_give/2))//1-mid<konf or k_give<0:
        right = mid
    else:
        left = mid

k_give=k_hodov-left
if ((k_give+1)*(k_give/2))//1-left==konf:
    print(left)
else:
    print(left-1)

































"""i=1
k_eat=0
last_give = 1
for i in range(arr[0]):
    if konf>=last_give:
        konf-=last_give
        last_give+=1
    else:
        k_eat+=1
        konf+=1
print(k_eat)"""