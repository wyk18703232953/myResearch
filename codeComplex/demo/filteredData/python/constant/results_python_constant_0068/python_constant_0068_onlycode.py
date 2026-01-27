n = int(input())
if n==0:
    print(*[0,0,0])
elif n==1:
    print(*[0,0,1])
else:
    prev2 = 0
    prev1 = 1
    prev = 1
    while prev!=n:
        curr = prev+prev1
        prev2 = prev1
        prev1 = prev
        prev = curr
    print(*[0,prev2,prev1])
