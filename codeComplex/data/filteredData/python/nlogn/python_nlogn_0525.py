def main(n):
    t = n
    results = []
    for case in range(t):
        # deterministically define array size for this test
        length = case + 4
        # generate deterministic array values
        a = [((i * 3 + case) % 50) + 1 for i in range(length)]

        if len(set(a)) == 1:
            x = a[0]
            results.append(f"{x} {x} {x} {x}")
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
                results.append(f"{mx} {mx} {mx} {mx}")
            else:
                res = []
                for k in d:
                    if d[k] >= 2:
                        res.append(k)
                m = len(res)
                if m < 2:
                    # fallback: repeat smallest element when not enough pairs
                    if a:
                        x = a[0]
                    else:
                        x = 0
                    results.append(f"{x} {x} {x} {x}")
                else:
                    minj = 0
                    for j in range(m - 1):
                        lhs = res[j] * res[j+1] * (res[minj]**2 + res[minj+1]**2)
                        rhs = res[minj] * res[minj+1] * (res[j]**2 + res[j+1]**2)
                        if lhs > rhs:
                            minj = j
                    x, y = res[minj], res[minj+1]
                    results.append(f"{x} {x} {y} {y}")
    print("\n".join(results))


if __name__ == "__main__":
    main(5)