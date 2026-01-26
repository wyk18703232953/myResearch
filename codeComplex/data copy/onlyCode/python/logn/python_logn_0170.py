import sys
import math


def readlines(type=int):
    return list(map(type, sys.stdin.readline().split()))


def read(type=int):
    return type(sys.stdin.readline().strip())


joint = lambda it, sep=" ": sep.join(
    [str(i) if type(i) != list else sep.join(map(str, i)) for i in it])


def solve_naive(n, k):
    taken = set()
    current_cap = 0
    found = False
    while current_cap != n:
        for c in range(k, 1, -1):
            found = False
            if current_cap == 0:
                if c <= n:
                    current_cap += c
                    taken.add(c)
                    found = True
                    break
            else:
                if c not in taken and c - 1 <= n - current_cap:
                    current_cap += c - 1
                    taken.add(c)
                    found = True
                    break
        if not found:
            break
    return len(taken) if found else -1


def solve(n, k):
    if n == 1:
        return 0
    if k >= n:
        return 1
    else:
        if (3 - 2 * k) ** 2 - 8 * (n - k) < 0:
            return -1
        t = (-math.sqrt((3 - 2 * k) ** 2 - 8 * (n - k)) + (2 * k) - 3) / 2
        if t == 0.0:
            return 2
        if t % 1 == 0:
            return 1 + int(t)
        else:
            # print(f"{t=}")
            return 2 + int(t)


def main():
    n, k = readlines()
    print(solve(n, k))


if __name__ == "__main__":
    main()
