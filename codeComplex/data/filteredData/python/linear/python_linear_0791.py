#!/usr/bin/env python3

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

def build_arrays(n, k):
    a = [0]
    base = (n ^ (k * 3)) % 10
    for i in range(1, n + 1):
        a.append((base + (i * (k + 1))) % 10)
    l = [0 for _ in range(n + 1)]
    r = [0 for _ in range(n + 1)]
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
    return a, l, r

def main(n):
    if n <= 0:
        return
    k = (n // 3) + 1
    if k > n:
        k = n
    a, l, r = build_arrays(n, k)
    if win1(n, k, a, l, r):
        print("tokitsukaze")
    elif win2(n, k, a, l, r):
        print("quailty")
    else:
        print("once again")

if __name__ == "__main__":
    main(10)