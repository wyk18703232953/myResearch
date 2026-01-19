import sys

def solve(a):
    n = len(a)
    if n == 0:
        return 0, 0
    m = len(a[0]) if a[0] else 0

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
    res_i, res_j = 0, 0
    while right - left > 1:
        mid = (right + left) // 2
        flag, (q1, q2) = check(mid)
        if flag:
            left = mid
            res_i, res_j = q1, q2
        else:
            right = mid
    return res_i + 1, res_j + 1


def generate_data(n):
    if n <= 0:
        return []
    # Define matrix dimensions deterministically from n
    # n = number of rows; m derived from n to allow scaling
    m = max(1, n // 2 + 1)
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic value depending on (i, j) and n
            # Keeps values within a reasonable range while varying with n
            val = (i * (j + 1) + j * j + n) % (10**6)
            row.append(val)
        a.append(row)
    return a


def main(n):
    a = generate_data(n)
    i, j = solve(a)
    print(i, j)


if __name__ == "__main__":
    main(5)