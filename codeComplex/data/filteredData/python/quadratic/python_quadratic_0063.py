import random

def main(n):
    # 1. 生成规模为 n 的测试数据 values
    # 例如生成 1~n 的随机排列
    values = list(range(1, n + 1))
    random.shuffle(values)

    # 2. 计算初始逆序对个数 cnt
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] > values[j]:
                cnt += 1

    # 3. 生成查询数量 m 以及每个查询的区间 [l, r]
    # 这里示例生成 m = n 个查询，每个查询随机区间
    m = n
    queries = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 4. 按原逻辑处理每个查询并输出结果
    for l, r in queries:
        length = r - l + 1
        cnt += length * (length - 1) // 2
        cnt &= 1
        if cnt == 1:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)