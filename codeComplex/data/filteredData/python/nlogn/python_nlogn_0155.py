def main(n):
    # 映射关系：
    # 原程序中有 n, k 和长度为 n 的数组 l
    # 这里将输入规模参数 n 直接作为数组长度
    # k 使用一个确定性的函数，例如 k = n + 1（且避免为 0）
    k = n + 1 if n >= 0 else 1

    # 构造确定性数组 l，长度为 n
    # 使用简单的算术构造，如 (3*i + 1) % (2*n + 1)，避免过大数值且确保多样性
    # 当 n = 0 时，l 为空列表
    if n > 0:
        l = [(3 * i + 1) % (2 * n + 1) for i in range(n)]

    else:
        l = []

    d = dict()
    c = set()
    l.sort()
    for i in range(n):
        if not d.get(l[i]):
            c.add(l[i])
            d.setdefault(l[i] * k, 1)
    # print(len(c))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模实验
    main(10)