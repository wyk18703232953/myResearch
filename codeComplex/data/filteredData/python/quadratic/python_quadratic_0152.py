from itertools import permutations as p
import random

# 模拟原来 rd()：逐个产生整数
def rd(seq_iter):
    for ch in seq_iter:
        yield ch

def f(n, t, data_iter):
    a = 0
    f_flag = 1
    # 共需要读取 2*n 个数（因为原来是 n 行，每行两位）
    for _ in range(n):
        for x in rd(next(data_iter)):
            if x != f_flag:
                a += 1
            f_flag = 1 - f_flag
    # t < 3 时额外读一行丢弃
    if t < 3:
        _ = next(data_iter)
    return a

def main(n):
    # 生成测试数据：
    # 总共需要读取 4 轮 f(n,t)
    # 每轮：
    #   读 n 行，每行两位 -> n
    #   若 t < 3 再读 1 行 -> 3
    # 所以共 4*n + 3 行，每行 2 个 0/1
    total_lines = 4 * n + 3
    raw_lines = []
    for _ in range(total_lines):
        # 每一“行”生成两个 0/1，拼成字符串，如 "01"
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        raw_lines.append(f"{a}{b}")

    # 用迭代器模拟输入行
    data_iter = iter(raw_lines)

    m = []
    b_vec = [-1, -1, 1, 1]
    for t in range(4):
        m.append(f(n, t, data_iter))

    # 最终计算与输出
    res = 2 * n ** 2 + min(
        sum(x * y for x, y in zip(q, m))
        for q in set(p(b_vec))
    )
    print(res)


if __name__ == "__main__":
    # 示例：规模设为 5，可根据需要修改
    main(5)