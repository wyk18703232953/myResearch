import sys
import random

def main(n):
    # 生成测试数据：根据题意，a 和 b 至少有一个为 1，且不同时 >1
    # 这里随机生成符合约束的 a, b
    if n <= 3:
        # 小规模时，避免生成必然 NO 的特例太多，这里仍保持随机但受限
        candidates = []
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if not (a > 1 and b > 1):
                    candidates.append((a, b))
        a, b = random.choice(candidates)
    else:
        # 对于较大 n，优先生成更有结构的情况
        if random.random() < 0.5:
            a, b = 1, random.randint(1, n)
        else:
            a, b = random.randint(1, n), 1

    # 以下为原逻辑，移除 input() 后直接使用生成的 n, a, b
    if a > 1 and b > 1:
        print('NO')
        return

    if n == 3 and a == 1 and b == 1:
        print('NO')
        return

    if n == 2 and a == 1 and b == 1:
        print('NO')
        return

    t = [[0 for _ in range(n)] for _ in range(n)]

    comp = max(a, b)

    for i in range(comp - 1, n - 1):
        t[i][i + 1] = 1
        t[i + 1][i] = 1

    if b > 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    t[i][j] = 1 - t[i][j]

    print('YES')
    for i in range(n):
        print("".join(map(str, t[i])))


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(5)