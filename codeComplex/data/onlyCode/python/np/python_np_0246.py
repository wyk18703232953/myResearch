import sys
from array import array  # noqa: F401
import typing as Tp  # noqa: F401


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


def output(*args):
    sys.stdout.buffer.write(
        ('\n'.join(map(str, args)) + '\n').encode('utf-8')
    )


def main():
    n, m, k = map(int, input().split())
    a = list(map(float, input().split()))
    add = [[0] * n for _ in range(n + 1)]
    for xi, yi, ci in (map(int, input().split()) for _ in range(k)):
        add[xi - 1][yi - 1] = float(ci)

    minf = float('-inf')
    dp = [[minf] * (2**n) for _ in range(n + 1)]
    dp[n][0] = 0.0

    for bitset in range(2**n):
        if bin(bitset).count('1') >= m:
            continue

        for i in range(n + 1):
            if dp[i][bitset] == minf:
                continue
            for j in range(n):
                if (1 << j) & bitset:
                    continue
                dp[j][bitset | (1 << j)] = max(
                    dp[j][bitset | (1 << j)],
                    dp[i][bitset] + a[j] + add[i][j]
                )

    print(int(max(max(_dp) for _dp in dp) + 1e-7))


if __name__ == '__main__':
    main()
