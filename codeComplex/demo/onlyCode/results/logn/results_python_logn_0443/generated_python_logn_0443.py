def main(n):
    t = n
    results = []
    for case in range(1, t + 1):
        k = case
        if n > 31:
            results.append(("YES", n - 1))
            continue
        else:
            if k > (4 ** n - 1) // 3:
                results.append(("NO",))
                continue
        l = (4 ** n - 1) // 3
        i = 1
        j = 0
        k_work = k
        while i <= n:
            k_work -= (2 ** i - 1)
            j = i
            if k_work < 0:
                j = j - 1
                k_work += (2 ** i - 1)
                break
            i += 1
        k2 = k - k_work
        k3 = (2 ** (j + 1) - 1) * ((4 ** (n - j) - 1) // 3)
        if l - k2 - k3 >= k_work:
            results.append(("YES", n - i + 1))
        else:
            results.append(("NO",))
    return results

if __name__ == "__main__":
    out = main(10)
    for r in out:
        print(*r)