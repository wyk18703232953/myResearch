def main(n):
    t = n
    results = []
    for case_idx in range(1, t + 1):
        size = case_idx
        a = [1 + (i % (case_idx + 2)) for i in range(size)]
        if len(set(a)) == 1:
            results.append(f"{a[0]} {a[0]} {a[0]} {a[0]}")

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
                results.append(f"{mx} {mx} {mx} {mx}")

            else:
                res = []
                for k in d:
                    if d[k] >= 2:
                        res.append(k)
                m = len(res)
                if m < 2:
                    # Fallback: repeat the only available value or default to 1
                    if m == 0:
                        x = 1
                        results.append(f"{x} {x} {x} {x}")

                    else:
                        x = res[0]
                        results.append(f"{x} {x} {x} {x}")

                else:
                    minj = 0
                    for j in range(m - 1):
                        left_num = res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2)
                        right_num = res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2)
                        if left_num > right_num:
                            minj = j
                    results.append(f"{res[minj]} {res[minj]} {res[minj+1]} {res[minj+1]}")
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(5)