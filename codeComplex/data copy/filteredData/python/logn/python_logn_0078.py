def main(n: int):
    # 根据规模 n 生成测试数据：
    # 让 r 为 n，l 为 [0, n] 区间内的一个值，保证 l <= r
    l = n // 2
    r = n

    n1 = bin(l)[2:]
    n2 = bin(r)[2:]

    if l == r:
        ans = 0
    elif len(n1) < len(n2):
        ans = int(len(n2) * '1', 2)

    else:
        index = 0
        for i in range(len(n1)):
            if n1[i] != n2[i]:
                index = i
                break
        ans = int((len(n1) - index) * '1', 2)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)