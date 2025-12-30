def main(n: int):
    # 根据 n 生成测试数据：生成 1..n 的整数列表，并打乱顺序
    import random

    l = list(range(1, n + 1))
    random.shuffle(l)

    # 下面是原始逻辑的封装
    l = sorted(l)
    seen = [False] * n
    res = 0
    for i in range(n):
        if seen[i]:
            continue
        res += 1
        for j in range(i, n):
            if l[j] % l[i] == 0:
                seen[j] = True
    print(res)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)