import io
import os

def solve(n, m, A):
    ans = ()
    nstats = 2 ** m

    def judge(finalScore):
        nonlocal ans
        seen = {}
        for i, scores in enumerate(A):
            sta = 0
            for e in scores:
                sta = sta * 2 + (e >= finalScore)
            seen[sta] = i

        for i in range(nstats):
            for j in range(nstats):
                if (i | j) == nstats - 1 and i in seen and j in seen:
                    ans = (seen[i], seen[j])
                    return True
        return False

    l = 0
    r = 2 ** 31 - 1
    while l < r:
        mid = l + (r - l) // 2
        if not judge(mid):
            r = mid
        else:
            l = mid + 1
    print(ans[0] + 1, ans[1] + 1)


def main(n):
    m = 5
    A = []
    for i in range(n):
        row = [((i + 1) * (j + 2)) % 100 for j in range(m)]
        A.append(row)
    solve(n, m, A)


if __name__ == "__main__":
    main(8)