import random

def main(n):
    # 生成测试数据
    # 约定：m 为不同元素的目标个数，取 1 到 n 之间的随机值
    if n <= 0:
        # 原逻辑中 n 至少应能容纳 m 个元素，n<=0 无意义，直接返回
        print(-1, -1)
        return

    m = random.randint(1, n)  # 确保 m <= n

    # 生成数组：为了尽量有机会出现至少 m 个不同元素，
    # 生成范围稍大一些
    arr = [random.randint(1, 2 * n) for _ in range(n)]

    # 原逻辑开始
    d = {}
    i = 1
    for x in arr:
        if len(d) == m:
            break
        if x not in d:
            d[x] = i
        i += 1

    if len(d) == m:
        print(min(d.values()), max(d.values()))
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)