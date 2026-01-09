def main(n):
    # Deterministically generate a, b based on n
    # Ensure coverage of different branches as n changes
    if n == 1:
        a, b = 1, 1
    elif n == 2:
        a, b = 1, 2
    elif n == 3:
        a, b = 2, 1

    else:
        # For n >= 4, cycle through some deterministic (a,b) pairs
        # based on n modulo 4 to vary behavior but remain deterministic
        r = n % 4
        if r == 0:
            a, b = 1, 1
        elif r == 1:
            a, b = 1, 2
        elif r == 2:
            a, b = 2, 1
        else:  # r == 3
            a, b = 2, 2

    # Core logic from original program
    if min(a, b) > 1:
        # print('NO')
        pass
        return

    m = max(a, b)

    if m == 1:
        if n == 1:
            # print('YES')
            pass
            # print(0)
            pass
            return
        elif n < 4:
            # print('NO')
            pass
            return

        else:
            # print('YES')
            pass
            for row in range(n):
                line = ['0'] * n
                if row > 0:
                    line[row - 1] = '1'
                if row < n - 1:
                    line[row + 1] = '1'
                # print(''.join(line))
                pass
        return

    # print('YES')
    pass

    if a == 1:
        c = '1'
        d = '0'

    else:
        c = '0'
        d = '1'
    for row in range(n):
        if row < m - 1:
            line = [c] * n

        else:
            line = [c] * (m - 1) + [d] * (n - m + 1)
        line[row] = '0'
        # print(''.join(line))
        pass
if __name__ == "__main__":
    main(10)