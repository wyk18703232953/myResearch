input();a=sorted(map(int,input().split()));s=c=0
while s<=sum(a):s+=a.pop();c+=1
print(c)