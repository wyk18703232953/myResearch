def main(n):
    # 生成确定性的输入列表 l1，长度为 n
    # 模式：前半部分为正整数，后半部分为 0 和重复值的混合
    if n <= 0:
        l1 = []

    else:
        half = n // 2
        # 前半段：1,2,3,...,half
        first_part = [i + 1 for i in range(half)]
        # 后半段：构造一些 0 和重复值
        remaining = n - half
        second_part = [(i % 3) for i in range(remaining)]
        l1 = first_part + second_part

    # 原算法逻辑
    if len(l1) > 0 and len(list(set(l1))) == 1 and l1[0] > 0:
        # print(1)
        pass

    else:
        l2 = list(set(l1))
        x = l1.count(0) if l1 else 0
        if x == 0:
            # print(len(l2))
            pass

        else:
            # print(len(l2) - 1)
            pass
if __name__ == "__main__":
    main(10)