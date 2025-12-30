import random

def main(n):
    # 生成测试数据：n 行 (a, b)，以及总容量 m
    # 约束：0 <= b <= a，保证 a-b 为非负；m 随机在 [0, sum(a)] 范围内
    a_vals = []
    b_vals = []
    for _ in range(n):
        a = random.randint(0, 1000)
        b = random.randint(0, a)
        a_vals.append(a)
        b_vals.append(b)
    m = random.randint(0, sum(a_vals))

    # 原逻辑开始
    space = 0
    saved = []
    for i in range(n):
        a = a_vals[i]
        b = b_vals[i]
        space += a
        saved.append(a - b)

    saved.sort(reverse=True)

    # 如果所有压缩都用上仍然大于 m，则输出 -1
    if space - sum(saved) > m:
        print(-1)
        return

    # 如果本来就不超过 m，则不需要压缩
    if space <= m:
        print(0)
        return

    # 否则依次使用压缩，直到 space <= m
    count = 0
    i = 0
    while i < n:
        count += 1
        space -= saved[i]
        if space <= m:
            print(count)
            return
        i += 1

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)