def ch_x(stri, n):
    res = ''
    for i in range(len(stri)):
        if i != n:
            res += stri[i]
        else:
            res += 'x'
    return res


a = input()
b = input()
n = 0
for i in range(0, len(a)):
    if a[i] == '0' and b[i] == '0':
        c = [i-1, i+1]
        for e in c:
            if 0 <= e < len(a):
                if a[e] == '0':
                    n += 1
                    a = ch_x(a, e)
                    break
                if b[e] == '0':
                    n += 1
                    b = ch_x(b, e)
                    break
        a = ch_x(a, i)
        b = ch_x(b, i)
print(n)