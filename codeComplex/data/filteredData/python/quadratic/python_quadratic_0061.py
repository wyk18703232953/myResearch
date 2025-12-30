import random

def main(n: int):
    # 1. 生成测试数据
    # 生成长度为 n 的数组，元素范围 1..n
    arr = [random.randint(1, n) for _ in range(n)]
    # 生成查询次数 q，这里设为 n（也可按需调整）
    q = n
    # 生成 q 个区间 [l, r]，1 <= l <= r <= n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2. 计算初始逆序奇偶性
    inv = 0
    for i in range(n):
        for j in range(n):
            if i < j and arr[i] > arr[j]:
                inv += 1
            inv = inv % 2  # 只保留奇偶性

    # 3. 处理查询并输出结果
    for l, r in queries:
        diff = r - l
        s = diff // 2
        if diff % 2:
            s += 1
        inv = (inv + (s % 2)) % 2
        if inv:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可按需修改 n
    main(5)