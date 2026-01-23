#!/usr/bin/env python3
import sys

def has_intersection(l1, r1, l2, r2):
    if l1 <= l2 and r2 <= r1:
        return True
    if l2 <= l1 and r1 <= r2:
        return True
    return False

def build_array(n):
    # construct an array A[0..n-1] such that for all i:
    # A[(i + n//2) % n] = A[i] + 1
    # a simple deterministic construction:
    # A[i] = i for 0 <= i < n//2
    # A[i] = i + 1 for n//2 <= i < n
    a = [0] * n
    half = n // 2
    for i in range(half):
        a[i] = i
    for i in range(half, n):
        a[i] = i + 1
    return a

def main(n):
    # n must be even and >= 2 to match original constraints
    if n < 2 or n % 2 != 0:
        return

    if (n // 2) % 2 == 1:
        print(-1)
        return
    # n is now divisible by 4
    a = build_array(n)

    def ask(i):
        return a[i]

    l1 = 0
    r1 = n // 2
    a_l1 = ask(l1)
    a_r1 = ask(r1)
    if a_l1 == a_r1:
        print(0)
        return
    a_l2 = a_r1
    a_r2 = a_l1
    while True:
        m1 = (l1 + r1) // 2
        m2 = (m1 + n // 2) % n
        a_m1 = ask(m1)
        a_m2 = ask(m2)
        if a_m1 == a_m2:
            print(m1 + 1)
            return
        if has_intersection(a_l1, a_m1, a_l2, a_m2):
            r1 = m1
            a_r1 = a_m1
            a_r2 = a_m2
        else:
            assert has_intersection(a_m1, a_r1, a_m2, a_r2)
            l1 = m1
            a_l1 = a_m1
            a_l2 = a_m2

if __name__ == "__main__":
    # example deterministic call for time-complexity experiments
    main(16)