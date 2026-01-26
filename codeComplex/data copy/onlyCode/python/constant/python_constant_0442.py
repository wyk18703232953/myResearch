n, m = map(int, input().split())

a = []
b = []

if n <= 8:
    a = [4]
    b = [5]
    
while n > 8:
    a += [4,5]
    b += [5,4]
    n -= 8
    
print(*a + [5], sep="")
print(*b + [5], sep="")