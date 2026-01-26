def main(n):
    # 生成确定性的输入数据：长度为 n 的整数列表
    # 使用一个简单的周期性构造，保证有重复元素和非最小元素
    ls = [(i * 2) % (n // 2 + 1 if n > 1 else 1) for i in range(n)]

    # 原始逻辑开始
    ls.sort()
    if ls.count(min(ls)) == len(ls):
        # print('NO')
        pass
    for i in range(n):
        if ls[i] != min(ls):
            # print(ls[i])
            pass
            break


if __name__ == "__main__":
    main(10)