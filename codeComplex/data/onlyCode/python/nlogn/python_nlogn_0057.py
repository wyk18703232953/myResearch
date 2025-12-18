s = input()
l = list(map(int,input().split()))
l.sort(reverse = True)
s = sum(l)
x = 0 
c = 0
for i in l:
    if x <= s:
        c+=1
        x+=i
        s-=i
    else:
        break
print(c)