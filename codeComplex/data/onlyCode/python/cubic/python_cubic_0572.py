a = [ord(e) - ord('0') for e in list(input().strip())]
b = [ord(e) - ord('0') for e in list(input().strip())]

a.sort(reverse=True)
h = [0 for i in range(10)]
for x in a:
    h[x] += 1

if len(a) < len(b):
    print(''.join(map(str, a)))
    exit(0)

def gmax(hx):
    s = list(hx)
    res = list()
    for i in range(9, -1, -1):
        while s[i] > 0:
            res.append(i)
            s[i] -= 1
    return res

def gmin(hx):
    s = list(hx)
    res = list()
    for i in range(10):
        while s[i] > 0:
            res.append(i)
            s[i] -= 1
    return res

res = list()

def finalize(x):
    for y in range(x-1, -1, -1):
        if h[y] > 0:
            res.append(y)
            h[y] -= 1
            for i in range(9, -1, -1):
                while h[i] > 0:
                    res.append(i)
                    h[i] -= 1
            return

p = 0
while p < len(a):
    x = b[p]    
    if h[x] > 0:
        hh = list(h)
        hh[x] -= 1
        if b[p+1:] >= gmin(hh): # can make a smaller one with the remainings
            res.append(x)
            h[x] -= 1
        else:
            finalize(x)
            break
    else:
        finalize(x)
        break
    p += 1
print(''.join(map(str, res)))