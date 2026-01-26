n=int(input())
l=list(map(int,input().split(' ')))
l.sort(reverse=True)
#print(l)
coin=0
total_sum=sum(l)
current_sum=0
for i in range(len(l)):
    coin+=1
    current_sum=current_sum+l[i]
    remaining_sum=total_sum-current_sum
    if current_sum>remaining_sum:
        break
print(coin)