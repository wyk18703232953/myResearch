def main(n):
    a = list(range(n))
    s = set()
    s.add(-1)
    a = [-1] + a
    a.sort()
    count, add = 0, 0
    flag = 0
    for i in range(1, n + 1):
        if a[i] in s and a[i] - 1 in s:
            flag = 1
            break
        if a[i] in s:
            add += 1
        if add == 2:
            flag = 1
            break
        s.add(a[i])
        count += a[i] - (i - 1)
    if flag == 0 and count % 2 == 1:
        return "sjfnb"
    else:
        return "cslnb"