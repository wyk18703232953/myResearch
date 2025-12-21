def main(n):
    t = n
    results = []
    for _ in range(t):
        n_val = n
        k = (4 ** n_val - 1) // 3
        if n_val > 31:
            results.append(("YES", n_val - 1))
            continue
        else:
            if k > (4 ** n_val - 1) // 3:
                results.append(("NO",))
                continue
        l = (4 ** n_val - 1) // 3
        i = 1
        j = 0
        k1 = k
        while i <= n_val:
            k -= (2 ** i - 1)
            j = i
            if k < 0:
                j = j - 1
                k += (2 ** i - 1)
                break
            i += 1
        k2 = k1 - k
        k3 = (2 ** (j + 1) - 1) * ((4 ** (n_val - j) - 1) // 3)
        if l - k2 - k3 >= k:
            results.append(("YES", n_val - i + 1))
        else:
            results.append(("NO",))
    return results

if __name__ == "__main__":
    print(main(5))