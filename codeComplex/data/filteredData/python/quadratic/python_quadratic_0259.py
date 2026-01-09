def main(n):
    # Deterministically generate a, b from n
    # Ensure a, b >= 1 and not both 1 all the time to exercise branches
    a = (n % 5) + 1
    b = (n % 7) + 1

    from collections import defaultdict
    hash_map = defaultdict(list)  # kept to preserve original structure, though unused

    # Original logic starts here
    if a == 1 and b == 1:
        if n == 2 or n == 3:
            # print('NO')
            pass
            return

    if a == 1 or b == 1:
        bool_arr = [False] * (n + 1)

        if a > n or b > n:
            # print('NO')
            pass
            return
        # print('YES')
        pass

        l = []
        for _ in range(n):
            z = ['0'] * n
            l.append(z)
        ans = []
        for _ in range(n):
            z = ['0'] * n
            ans.append(z)

        if b == 1:
            for i in range(a - 1, n - 1):
                l[i][i + 1] = '1'
                l[i + 1][i] = '1'

            for row in l:
                # print(''.join(row))
                pass

        else:
            ans = []
            for _ in range(n):
                z = ['0'] * n
                ans.append(z)

            for i in range(b - 1, n - 1):
                l[i][i + 1] = '1'
                l[i + 1][i] = '1'

            for i in range(n):
                for j in range(n):
                    if i != j:
                        if l[i][j] == '1':
                            ans[i][j] = '0'
                        if l[i][j] == '0':
                            ans[i][j] = '1'

            for row in ans:
                # print(''.join(row))
                pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)