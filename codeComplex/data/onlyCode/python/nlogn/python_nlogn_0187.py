import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1

    ans = 0
    for i in range(N):
        a = A[i]
        cnt[a] -= 1
        sum_A -= a

        tmp = sum_A
        n = 0
        for b in (a-1, a, a+1):
            n += cnt[b]
            tmp -= b * cnt[b]
        ans += tmp - a * (N-1-i-n)
    print(ans)


if __name__ == "__main__":
    main()
