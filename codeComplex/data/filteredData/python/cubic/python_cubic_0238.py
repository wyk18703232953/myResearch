from random import randint

def main(n: int):
    # 1. 生成测试数据：
    #    将 n 拆成 3 份作为 R,G,B 的规模（保证每个 >=1）
    #    多余的部分依次加到 R,G,B 上
    base = max(1, n // 3)
    R = G = B = base
    rest = max(0, n - 3 * base)
    if rest > 0:
        R += 1
        rest -= 1
    if rest > 0:
        G += 1
        rest -= 1
    if rest > 0:
        B += 1
        rest -= 1

    # 生成 R,G,B 数组（正整数）
    Ra = sorted([randint(1, 10**6) for _ in range(R)], reverse=True)
    Ga = sorted([randint(1, 10**6) for _ in range(G)], reverse=True)
    Ba = sorted([randint(1, 10**6) for _ in range(B)], reverse=True)

    # 2. 原逻辑迁移（去掉 input/输出改为 return）：
    final_ans = 0

    # 三维 DP 数组，初始化为 -1
    dparr = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    # 初始三个状态
    dparr[1][1][0] = Ra[0] * Ga[0]
    dparr[1][0][1] = Ra[0] * Ba[0]
    dparr[0][1][1] = Ga[0] * Ba[0]
    final_ans = max(final_ans, dparr[1][1][0], dparr[1][0][1], dparr[0][1][1])

    # 内部函数访问外部变量
    def add_ns(t1, queue):
        x, y, z = t1
        # (x+1, y+1, z)
        if x + 1 <= R:
            if y + 1 <= G:
                if dparr[x + 1][y + 1][z] == -1:
                    queue.append((x + 1, y + 1, z))
                    dparr[x + 1][y + 1][z] = 0
            # (x+1, y, z+1)
            if z + 1 <= B:
                if dparr[x + 1][y][z + 1] == -1:
                    queue.append((x + 1, y, z + 1))
                    dparr[x + 1][y][z + 1] = 0
        # (x, y+1, z+1)
        if y + 1 <= G and z + 1 <= B:
            if dparr[x][y + 1][z + 1] == -1:
                queue.append((x, y + 1, z + 1))
                dparr[x][y + 1][z + 1] = 0

    def store_ans(t1):
        nonlocal final_ans
        x, y, z = t1

        if x - 1 >= 0 and y - 1 >= 0 and z >= 0 and dparr[x - 1][y - 1][z] != -1:
            dparr[x][y][z] = max(
                dparr[x][y][z],
                dparr[x - 1][y - 1][z] + Ra[x - 1] * Ga[y - 1],
            )
        if x - 1 >= 0 and y >= 0 and z - 1 >= 0 and dparr[x - 1][y][z - 1] != -1:
            dparr[x][y][z] = max(
                dparr[x][y][z],
                dparr[x - 1][y][z - 1] + Ra[x - 1] * Ba[z - 1],
            )
        if x >= 0 and y - 1 >= 0 and z - 1 >= 0 and dparr[x][y - 1][z - 1] != -1:
            dparr[x][y][z] = max(
                dparr[x][y][z],
                dparr[x][y - 1][z - 1] + Ga[y - 1] * Ba[z - 1],
            )

        final_ans = max(final_ans, dparr[x][y][z])

    # BFS 队列初始化
    queue = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
    add_ns(queue[0], queue)
    add_ns(queue[1], queue)
    add_ns(queue[2], queue)
    ptr = 3

    # 主循环
    while ptr < len(queue):
        store_ans(queue[ptr])
        add_ns(queue[ptr], queue)
        ptr += 1

    # 将结果返回（不再直接打印）
    return final_ans

# 示例：手动调用
if __name__ == "__main__":
    # 例如规模 n = 9
    ans = main(9)
    print(ans)