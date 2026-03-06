def main(n):
    # Interpret n as both number of rows and columns (n x n matrix)
    # Ensure m >= 1
    m = max(1, n)

    # Deterministic generation of matrix a (n rows, m columns)
    # Values grow with i, j to allow non-trivial behavior of the algorithm
    a = [[i * m + j for j in range(m)] for i in range(n)]

    def check(mid):
        mask = (1 << m) - 1
        s = set()
        d = {}
        for i in range(n):
            state = 0
            for j in range(m):
                if a[i][j] >= mid:
                    state += 1 << j
            if state in s:
                continue
            s.add(state)
            k = state
            while k >= 0:
                k &= state
                d[k] = i
                k -= 1
            need = mask ^ state
            if need in d:
                q1, q2 = d[need], i
                if q1 > q2:
                    q1, q2 = q2, q1
                return True, (q1, q2)
        return False, (-1, -1)

    left = 0
    right = 10**9 + 1
    i = 0
    j = 0
    while right - left > 1:
        mid = (right + left) // 2
        flag, (q1, q2) = check(mid)
        if flag:
            left = mid
            i, j = q1, q2
        else:
            right = mid

    # Return result to make function usable in experiments
    return i + 1, j + 1


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    res = main(10)
    print(res[0], res[1])