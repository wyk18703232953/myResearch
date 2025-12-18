def read_data():
    n = int(input().strip())
    a = []
    for i in range(n):
        line = tuple(map(int, input().strip().split()))
        a.append(line)
    return n, a

def is_on_line(a,b,c):
    return 1 if (a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1])) == 0 else 0

def solve():
    if n <= 4:
        return 1
    line1 = []
    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[0],a[1],a[i]):
            if len(line2) < 2:
                line2.append(i)
            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1
    line1 = []
    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[0],a[2],a[i]):
            if len(line2) < 2:
                line2.append(i)
            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1
    line1 = []
    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[1],a[2],a[i]):
            if len(line2) < 2:
                line2.append(i)
            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1
    return 0

n, a = read_data()
print("Yes" if solve() == 1 else "No")