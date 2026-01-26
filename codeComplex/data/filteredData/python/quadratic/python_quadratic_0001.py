import math


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def generate_input(n):
    if n <= 0:
        n = 1
    r = max(1, n // 5)
    a = [i * r for i in range(n)]
    return n, r, a


def main(n):
    n, r, a = generate_input(n)
    ans = []
    ans.append(r)
    for i in range(1, n):
        ymax = r
        for j in range(i):
            if abs(a[j] - a[i]) <= 2 * r:
                ymax = max(ymax, ans[j] + math.sqrt(4 * r * r - (a[i] - a[j]) ** 2))
        ans.append(ymax)
    # print(*ans)
    pass
    return


if __name__ == "__main__":
    main(10)