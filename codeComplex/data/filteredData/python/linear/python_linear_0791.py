def win1(n, k, a, l, r):
    if n == k or r[k + 1] == n or l[n - k] == 1:
        return True
    for i in range(2, n - k + 1):
        if l[i - 1] == 1 and r[i + k] == n and a[i - 1] == a[i + k]:
            return True
    return False

def win2(n, k, a, l, r):
    if 2 * k < n:
        return False
    for i in range(2, n - k + 1):
        if l[i - 1] != 1 or r[i + k] != n:
            return False
    return True

def run_logic(n, k, a):
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    l[1], r[n] = 1, n
    for i in range(2, n + 1):
        if a[i - 1] == a[i]:
            l[i] = l[i - 1]

        else:
            l[i] = i
        if a[n - i + 1] == a[n - i + 2]:
            r[n - i + 1] = r[n - i + 2]

        else:
            r[n - i + 1] = n - i + 1
    if win1(n, k, a, l, r):
        return "tokitsukaze"
    elif win2(n, k, a, l, r):
        return "quailty"

    else:
        return "once again"

def main(n):
    if n < 2:
        n = 2
    k = n // 2
    a = [0]
    for i in range(1, n + 1):
        a.append((i // 2) % 2)
    result = run_logic(n, k, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)