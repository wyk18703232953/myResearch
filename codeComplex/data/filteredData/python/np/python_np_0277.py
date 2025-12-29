import math
import random

p2 = [1] * 64
for i in range(1, 64):
    p2[i] = p2[i - 1] * 2

max_level = 0  # 将在 main(n) 中根据 n 更新


def find_level(x):
    x0 = 1
    for i in range(max_level + 1):
        if (x - x0) % (x0 * 2) == 0:
            return i
        x0 *= 2
    return max_level  # 理论上不会到这里，兜底返回


def move_U(number):
    cur_lv = find_level(number)

    if cur_lv == max_level:
        return number

    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg

    return (x0 * 2) + (index // 2) * (seg * 2)


def move_L(number):
    cur_lv = find_level(number)

    if cur_lv == 0:
        return number

    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg

    return (x0 // 2) + (index * 2) * (seg // 2)


def move_R(number):
    cur_lv = find_level(number)

    if cur_lv == 0:
        return number

    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg

    return (x0 // 2) + (index * 2 + 1) * (seg // 2)


def move(s, num):
    if s == 'U':
        return move_U(num)
    if s == 'L':
        return move_L(num)
    return move_R(num)


def process(S, num):
    for s in S:
        num = move(s, num)
    return num


def main(n):
    """
    使用规模 n 自动生成测试数据并运行原逻辑。
    假设原题 n 是满二叉树节点数，即 n = 2^(h+1) - 1。
    这里根据 n 计算 q，并随机生成 q 组 (num, S) 测试数据。
    """
    global max_level
    max_level = int(math.log2(n + 1)) - 1

    # 生成测试数据：
    # 令 q = min(n, 10)（示例策略，可按需要调整）
    q = min(n, 10)

    # 随机生成 q 个查询：
    # num: 1..n 之间的随机节点编号
    # S:  长度为 0..max_level 的随机操作序列，每个字符为 U/L/R
    ops = ['U', 'L', 'R']
    random.seed(0)  # 固定随机种子，保证可复现

    queries = []
    for _ in range(q):
        num = random.randint(1, n)
        length = random.randint(0, max(0, max_level))
        S = ''.join(random.choice(ops) for _ in range(length))
        queries.append((num, S))

    # 执行查询并收集结果
    ans_lines = []
    for num, S in queries:
        ans_lines.append(str(process(S, num)))

    # 打印结果（与原始程序行为一致：最后统一输出）
    print('\n'.join(ans_lines))


if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    # 例如对应原注释示例中 n=15：
    main(15)