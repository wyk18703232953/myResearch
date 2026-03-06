def main(n):
    # Interpret n as: n rows, m columns (for time complexity scaling)
    # Here we choose m as max(1, n.bit_length()) to let m grow slowly with n
    m = max(1, n.bit_length())

    # Deterministically generate matrix a of size n x m
    # Values are constructed so that they vary with i, j but are fully deterministic
    a = [[(i * 131 + j * 17) % 1000000000 for j in range(m)] for i in range(n)]

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
    i_res, j_res = 0, 0
    while right - left > 1:
        mid = (right + left) // 2
        flag, (q1, q2) = check(mid)
        if flag:
            left = mid
            i_res, j_res = q1, q2
        else:
            right = mid

    # Keep the original output behavior
    print(i_res + 1, j_res + 1)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(1000)