n=int(input())
arr=list(map(int, input().split()))
dict={}
rawsum=0
a=n-1
b=1
for i in range(n):
    if i == 0:
	    rawsum = rawsum - (arr[i] * (a))
	    a-=1
    elif i == n - 1:
        rawsum = rawsum + (arr[i] * (b))
        b+=1
    else:
        rawsum = rawsum + (arr[i] * (b))
        rawsum = rawsum - ((arr[i] * (a)))
        a-=1
        b+=1
i=n-1
while i>=0:
    if dict.get(arr[i])==None:
        dict[arr[i]]=1
    else:
        dict[arr[i]]=dict[arr[i]]+1
    s=arr[i]-1
    g=arr[i]+1
    if dict.get(s)!=None:
        rawsum+=dict[s]
    if dict.get(g)!=None:
        rawsum-=dict[g]
    i-=1
print(rawsum)