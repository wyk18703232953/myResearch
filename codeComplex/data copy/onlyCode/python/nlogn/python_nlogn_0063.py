n=int(input())
a=list(map(int,input().split()))
a.sort()
# print(a)
total_money=sum(a)
i_have=0
reaming=total_money-i_have
cnt=0
for i in range(n-1,-1,-1):
    reaming=total_money-i_have
    if i_have>reaming:
        break
    i_have+=a[i]
    cnt+=1
print(cnt)