def solve(a, b):
    m = len(a)
    n = len(b)
    p_b = [0]
    for x in b[:]:
        p_b.append(p_b[-1] + int(x))
    s = 0
    for i in range(m):
        if a[i] == '0':
            s += p_b[n - m + 1 + i] - p_b[i]
        else:
            s += (n - m + 1) - (p_b[n - m + 1 + i] - p_b[i])
    return s


a = input()
b = input()
print(solve(a, b))
