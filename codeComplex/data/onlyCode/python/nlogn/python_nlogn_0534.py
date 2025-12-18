import sys
input=sys.stdin.buffer.readline
n,k=map(int,input().split())
arr=list(map(int,input().split()))
d=[{} for i in range(11)]
for i in range(n):
    st=arr[i]
    for j in range(11):
        r=st % k
        try:
            d[j][r]+=1
        except KeyError:
            d[j][r] =1
        st*=10
count_pair=0
for i in arr:
    st=str(i)
    l=len(st)
    mod_st=(k-(i % k)) %k
    if mod_st in d[l]:
        count_pair +=d[l][mod_st]
        if int(st + st) %k==0:
            count_pair -=1
print(count_pair)