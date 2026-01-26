def BinarySearch(a, x):
    import bisect
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

    else:
        return -1

def main(n):
    # 确定性构造输入 x, k
    # 让 n 同时影响 x 和 k 的规模
    x = n
    k = n // 2

    if x == 0:
        # print(0)
        pass

    else:
        mod = (10**9) + 7
        a = pow(2, k, mod)
        b = ((2 * x) % mod - 1) % mod
        ans = ((a * b) % mod + 1) % mod
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)