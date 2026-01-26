def main(n):
    if n < 2:
        # print(0)
        pass
        return
    # 确定性构造长度为 n 的数组 a
    # 这里选择一个简单的线性序列，保持随 n 规模扩展
    a = [(i * 3 + 1) for i in range(n)]
    k = min(a[0], a[-1]) // (n - 1)
    for i in range(1, n - 1):
        k = min(k, min(a[0], a[i]) // i, min(a[i], a[-1]) // (n - 1 - i))
    # print(k)
    pass
if __name__ == "__main__":
    main(10)