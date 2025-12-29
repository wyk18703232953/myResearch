import random

def main(n: int) -> None:
    # 生成测试数据
    # 约束选择：1 ≤ l ≤ r ≤ n*1000，x ≤ 1000
    tasks = [random.randint(1, 1000) for _ in range(n)]
    l = random.randint(1, max(1, n * 500))
    r = random.randint(l, n * 1000)
    x = random.randint(0, 1000)

    cnt = 0
    # 枚举所有非空子集
    for num in range(1, 2 ** n):
        subset = []
        for i in range(n):
            if num & (1 << i):
                subset.append(tasks[i])

        s = sum(subset)
        if l <= s <= r and max(subset) - min(subset) >= x:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：n=10，可按需修改
    main(10)