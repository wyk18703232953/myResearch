a = sorted(input())
b = int(input())
a = a[::-1] #reverse a
p = ''
cnt = [0]*10

while a :
    for i, d in enumerate(a):
        n = p + d + "".join(sorted(a[:i]+a[i+1:]))
        if int(n) <= b :
            p += d
            a.pop(i)
            break
        
print(p)