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
    R, G, B = map(int, input().split())
    r_sticks = sorted(map(float, input().split()), reverse=True) + [0.0]
    g_sticks = sorted(map(float, input().split()), reverse=True) + [0.0]
    b_sticks = sorted(map(float, input().split()), reverse=True) + [0.0]

    dp = [[[0.0] * (B + 2) for _ in range(G + 2)] for _ in range(R + 2)]

    for ri in range(R + 1):
        for gi in range(G + 1):
            for bi in range(B + 1):
                dp[ri + 1][gi + 1][bi] = max(dp[ri + 1][gi + 1][bi], dp[ri][gi][bi] + r_sticks[ri] * g_sticks[gi])
                dp[ri + 1][gi][bi + 1] = max(dp[ri + 1][gi][bi + 1], dp[ri][gi][bi] + r_sticks[ri] * b_sticks[bi])
                dp[ri][gi + 1][bi + 1] = max(dp[ri][gi + 1][bi + 1], dp[ri][gi][bi] + g_sticks[gi] * b_sticks[bi])

    ans = max(max(max(dp[r][g][b] for b in range(B + 1)) for g in range(G + 1)) for r in range(R + 1))
    print(int(ans + 1e-6))


if __name__ == '__main__':
    main()
