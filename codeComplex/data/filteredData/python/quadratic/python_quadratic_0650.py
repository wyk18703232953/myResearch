def main(n: int) -> None:
    # 根据 n 生成测试数据：生成一个长度为 n 的正整数数组
    # 这里简单生成 1..n 的序列，作为示例测试数据
    a = list(range(1, n + 1))

    a.sort()
    counter = 0
    test = [False] * n
    for j in range(n):
        if not test[j]:
            for i in range(n):
                if not test[i] and a[i] % a[j] == 0:
                    test[i] = True
            counter += 1
    # print(counter)
    pass


# 示例：需要时可以手动调用
# main(5)