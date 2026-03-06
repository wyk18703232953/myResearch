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

        full_mask = nstats - 1
        for i in range(nstats):
            if i in seen:
                for j in range(nstats):
                    if (i | j) == full_mask and j in seen:
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
    # For scalability/time-complexity experiments:
    # We map n to:
    #   number of rows in A: n
    #   number of columns (m): fixed small value to keep 2^m manageable
    # Here we keep m = 5 as in original complexity comment.
    m = 5
    # Deterministically generate A of size n x m
    # Use a simple arithmetic pattern: A[i][j] = (i * (j + 1)) % 100
    A = [[(i * (j + 1)) % 100 for j in range(m)] for i in range(n)]
    solve(n, m, A)


if __name__ == "__main__":
    # Example deterministic call for experimentation; adjust n as needed
    main(1000)