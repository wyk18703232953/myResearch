def main(n):
    # 映射含义：
    # n -> 数组长度
    # m, k 根据 n 确定性生成
    # 生成一个严格递减的正整数数组 a，方便与原逻辑匹配
    a = [n * 2 - i for i in range(n)]
    m = n * (n + 1) // 2  # 目标值随规模增长
    k = n // 2            # 初始 k 随规模确定性变化

    a.sort(reverse=True)
    if sum(a) + k - n < m:
        # print(-1)
        pass
    elif k >= m:
        # print(0)
        pass

    else:
        for i in range(1, n + 1):
            if sum(a[:i]) + k - i >= m:
                # print(i)
                pass
                break


if __name__ == "__main__":
    main(10)