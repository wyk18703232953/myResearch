def main(n):
    if n <= 0:
        return
    t = n
    fixed_testcases = 3
    for case_idx in range(1, fixed_testcases + 1):
        length = n * case_idx
        if length <= 0:
            length = 1
        a = []
        if case_idx == 1:
            val = case_idx * n
            a = [val for _ in range(length)]
        elif case_idx == 2:
            base = n % 7 + 1
            a = [(base + (i // 2)) for i in range(length)]
        else:
            base = n % 5 + 2
            for i in range(length):
                if i % 6 == 0:
                    a.append(base)
                elif i % 6 == 1:
                    a.append(base)
                elif i % 6 == 2:
                    a.append(base + 1)
                elif i % 6 == 3:
                    a.append(base + 1)
                elif i % 6 == 4:
                    a.append(base + 2)
                else:
                    a.append(base + (i // 3) % 4)
        if len(set(a)) == 1:
            x = a[0]
            print(x, x, x, x)
        else:
            a.sort()
            g1 = False
            d = {}
            mx = 10001
            for v in a:
                if v not in d:
                    d[v] = 1
                else:
                    d[v] += 1
                if d[v] == 4:
                    g1 = True
                    if v < mx:
                        mx = v
            if g1:
                print(mx, mx, mx, mx)
            else:
                res = []
                for k in d:
                    if d[k] >= 2:
                        res.append(k)
                m = len(res)
                if m < 2:
                    x = a[0]
                    print(x, x, x, x)
                else:
                    minj = 0
                    for j in range(m - 1):
                        left = res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2)
                        right = res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2)
                        if left > right:
                            minj = j
                    print(res[minj], res[minj], res[minj + 1], res[minj + 1])


if __name__ == "__main__":
    main(5)