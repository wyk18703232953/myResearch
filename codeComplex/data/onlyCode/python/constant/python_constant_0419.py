a,b=list(map(int,input().split()))
c,d=(((b+1)//2)-1,(b-a-1))
print(c if d<0 else c-d if c>d else 0)
