import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成 n 对 (l, r)
    # 你也可以根据需要修改生成规则
    test_data = []
    for _ in range(n):
        # 生成 [0, 2^20) 范围内的随机整数对
        l = random.randint(0, 2**20 - 1)
        r = random.randint(0, 2**20 - 1)
        test_data.append((l, r))

    # 对每组 (l, r) 按原逻辑进行计算并输出
    for l, r in test_data:
        x = l ^ r
        a = 2
        if l == r:
            print(0)
        else:
            while a <= x:
                a *= 2
            print(a - 1)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组测试并输出结果
    main(5)