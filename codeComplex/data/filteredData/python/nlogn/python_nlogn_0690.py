def main(n):
    # 生成测试数据
    # 设定 M = n
    M = n

    # 生成 B，长度为 n，严格递增，确保有至少两个元素
    # 例如：B = [1, 2, ..., n]
    B = list(range(1, n + 1))

    # 生成 G，长度也为 n
    # 例如：G 的每个元素为 n（保证 mG >= mB，一般不会输出 -1）
    G = [n] * n

    B.sort()
    mB = B[-1]
    m2B = B[-2]
    mG = min(G)

    if mB > mG:
        # print(-1)
        pass
        return

    if mB == mG:
        # print(sum(B) * M + sum(G) - mB * M)
        pass
        return

    # print(sum(B) * M + sum(G) - mB * M + mB - m2B)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)