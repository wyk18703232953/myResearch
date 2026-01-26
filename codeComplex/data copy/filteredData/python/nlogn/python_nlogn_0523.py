def main(n):
    # Interpret n as: number of test cases, each with array length = n
    # Deterministic data generation: a simple pattern depending on test index and position
    t = n
    for case_id in range(t):
        size = n
        # Generate array a of length 'size'
        # Mix of repeated and varying values to exercise branches
        a = [(case_id + i * 3) % (n // 2 + 2) for i in range(size)]

        if len(set(a)) == 1:
            v = a[0]
            # print(v, v, v, v)
            pass

        else:
            a.sort()
            g1 = False
            d = {}
            mx = 10001
            for val in a:
                if val not in d:
                    d[val] = 1

                else:
                    d[val] += 1
                if d[val] == 4:
                    g1 = True
                    if val < mx:
                        mx = val
            if g1:
                # print(mx, mx, mx, mx)
                pass

            else:
                res = []
                for k in d:
                    if d[k] >= 2:
                        res.append(k)
                m = len(res)
                if m < 2:
                    # Degenerate case: no element appears twice; fall back deterministically
                    # pick first 4 elements of sorted a
                    x = a[0]
                    y = a[1] if size > 1 else a[0]
                    # print(x, x, y, y)
                    pass
                    continue
                minj = 0
                for j in range(m - 1):
                    if res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2) > res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2):
                        minj = j
                # print(res[minj], res[minj], res[minj + 1], res[minj + 1])
                pass
if __name__ == "__main__":
    main(10)