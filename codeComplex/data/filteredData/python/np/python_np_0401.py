def main(n):
    # Map n to matrix size: n = number of rows, m = number of columns
    if n <= 0:
        return
    m = max(1, n // 2)

    # Deterministically generate matrix a of size n x m
    # Values are in a moderate range so that binary search over [0, 10**9+1) is meaningful
    a = [[(i * m + j) * 7 % 1000 for j in range(m)] for i in range(n)]

    def check(mid):
        mask = (1 << m) - 1
        s = set()
        d = dict()
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
    i = j = 0
    while right - left > 1:
        mid = (right + left) // 2
        flag, (q1, q2) = check(mid)
        if flag:
            left = mid
            i, j = q1, q2
        else:
            right = mid

    print(i + 1, j + 1)


if __name__ == "__main__":
    main(10)