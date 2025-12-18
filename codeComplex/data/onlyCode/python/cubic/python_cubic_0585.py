a = input()
b = input()

if len(a) < len(b):
    a = sorted(a)[::-1]
    print(''.join(a))
    exit(0)


def check(res, j, a):
    added = False
    tmp = ""
    for i in a:
        if i == j and not added:
            added = True
        else:
            tmp += i
    tmp = res + j + tmp[::-1]
    return tmp <= b


# len(a) == len(b)
res = ""
n = len(a)
a = sorted(list(a))[::-1]
for i in range(n):
    for j in a:
        if check(res, j, a):
            res += j
            a.remove(j)
            break
print(res)
