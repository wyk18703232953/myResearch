def main(n):
    # 将原程序的 n 视为字符串长度规模
    # 构造一个确定性的 k，保持 1 <= k < n，且不会等于 n
    if n <= 1:
        # print("")
        pass
        return

    k = n // 2
    if k >= n:
        k = n - 1

    d = (n - k) // 2 + 1
    x = ['1' if (i + 1) % d == 0 else '0' for i in range(n)]
    # print(''.join(x))
    pass
if __name__ == "__main__":
    main(10)