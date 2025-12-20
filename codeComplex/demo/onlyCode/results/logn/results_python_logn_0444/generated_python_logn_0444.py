def main(n):
    res = []
    for _ in range(n):
        # 生成测试用 n_val 和 k
        n_val = n
        # 使 k 在 1 到 (4**n_val-1)//3 范围内，保持与原算法同数量级
        limit = (4**n_val - 1) // 3 if n_val <= 31 else (4**31 - 1) // 3
        k = max(1, limit // 2)
        n_local = n_val
        k_local = k
        if n_local > 31:
            res.append(("YES", n_local - 1))
            continue
        else:
            if k_local > (4**n_local - 1) // 3:
                res.append(("NO",))
                continue
        l = (4**n_local - 1) // 3
        i = 1
        j = 0
        k_work = k_local
        while i <= n_local:
            k_work -= (2**i - 1)
            j = i
            if k_work < 0:
                j = j - 1
                k_work += (2**i - 1)
                break
            i += 1
        k2 = k_local - k_work
        k3 = (2**(j + 1) - 1) * ((4**(n_local - j) - 1) // 3)
        if l - k2 - k3 >= k_work:
            res.append(("YES", n_local - i + 1))
        else:
            res.append(("NO",))
    return res

if __name__ == "__main__":
    out = main(5)
    for item in out:
        print(*item)