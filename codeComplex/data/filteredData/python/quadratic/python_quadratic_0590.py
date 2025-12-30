import sys
import random

sss = 'RGB' * 700  # pattern base


def check(ss, p):
    i = 0
    m = 10 ** 5
    ans = 0
    while i < len(p):
        if p[i] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)

    ans = 0
    i = 1
    while i < len(p) + 1:
        if p[i - 1] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)

    ans = 0
    i = 2
    while i < len(p) + 2:
        if p[i - 2] != sss[i]:
            ans += 1
        i += 1
    m = min(m, ans)

    return m


def main(n):
    # n: problem size; we generate one test case.
    # Generate k in [1, n]
    if n <= 0:
        return

    k = random.randint(1, n)

    # Generate random string s of length n over 'R','G','B'
    chars = ['R', 'G', 'B']
    s = ''.join(random.choice(chars) for _ in range(n))

    m = 10 ** 5
    for i in range(n - k + 1):
        m = min(m, check(sss, s[i:i + k]))
    print(m)


if __name__ == "__main__":
    # Example: call main with a default size, can be changed as needed.
    main(10)