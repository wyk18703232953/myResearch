l,r=map(int,input().split())
for i in range(61)[::-1]:
  if (l>>i)&1!=(r>>i)&1:
    print((1<<(i+1))-1)
    exit()
print(0)