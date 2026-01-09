def main(n):
    # 将 n 映射为原程序中的 (n, k)
    # 保证 1 + (k*(k-1))//2 >= n，以避免输出 -1 或提前退出
    # 设 k = n，将原输入规模映射为 k 的大小，原始 n 固定为可由该 k 达到的最大值
    k = max(2, n)
    orig_n = 1 + (k * (k - 1)) // 2

    ini, fin = 1, k - 1

    if orig_n == 1:
        # print("0")
        pass
        return

    if 1 + (k * (k - 1)) // 2 < orig_n:
        # print("-1")
        pass
        return

    while ini < fin:
        mid = (ini + fin) // 2
        s = 1 + (k - 1) * mid - (mid * (mid - 1)) // 2
        if s >= orig_n:
            fin = mid

        else:
            ini = mid + 1

    # print(ini)
    pass
if __name__ == "__main__":
    main(10)