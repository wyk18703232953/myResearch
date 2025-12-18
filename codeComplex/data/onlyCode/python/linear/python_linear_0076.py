a = input()
b = input()
o = []
z = []
c0 = 0
c1 = 0
for i in b:
    if i == "0":
        c0 += 1

    else:
        c1 += 1

    o.append(c1)
    z.append(c0)

n = len(b)-1
m = len(a)-1
ans = 0
for i in range(len(a)):
    x = a[i]
    if x == "1":
        ans += z[(n-(m-i))]-z[i]
        if b[i] == "0":
            ans += 1

    else:
        ans += o[(n - (m - i))] - o[i]
        if b[i] == "1":
            ans += 1

print(ans)