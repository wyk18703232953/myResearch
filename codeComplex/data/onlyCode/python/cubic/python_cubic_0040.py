#// Remon Hasan, 19th sep '19
s = input()
n = len(s)
m = n - 1;
while m > 0:
    find = False
    for i in range(0, n - m):
        for j in range(i + 1, n - m + 1):
            match = True
            for k in range(0, m):
                if s[i+k] != s[j+k]:
                    match = False
                    break
            if match:
                find = True
                break
        if find:
            break
    if find:
        break
    m -= 1
print(m)
