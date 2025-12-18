# cook your dish here
n=int(input())
arr=[int(x) for x in input().split()]
li=arr[:]
li.sort()
c=0
for i in range(n):
    if(arr[i]!=li[i]):
        c+=1
    if(c>2):
        print("NO")
        break
else:
    print("YES")