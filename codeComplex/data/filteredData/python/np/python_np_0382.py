from collections import defaultdict
import random


def main(k: int):
    # --------------------------
    # 生成测试数据
    # --------------------------
    # 生成一个能保证有解的构造方式：
    # 1. 随机生成 k 行，每行长度随机在 [1, k+1]
    # 2. 随机生成一个 row_sum
    # 3. 对每一行，先随机生成若干数，再补一个值，使得该行和接近 row_sum
    #
    # 注意：原题对数据是有较强要求的，这里仅生成“形式上合理”的测试数据，
    # 不保证每次都一定有解，只是给 main 提供可运行的随机输入。
    data = defaultdict(list)
    position = defaultdict()
    nxt = defaultdict()
    agg_sum = list()

    # 随机行和的目标值
    row_sum = random.randint(5, 20)

    total_sum = 0
    for i in range(k):
        # 每行长度 1 ~ k+1
        length = random.randint(1, max(1, k + 1))
        row = []

        # 先生成 length-1 个随机数
        for _ in range(max(0, length - 1)):
            v = random.randint(-10, 10)
            row.append(v)

        # 最后一个数做一些偏移，让各行和分布在 row_sum 附近
        current_sum = sum(row)
        last_v = row_sum - current_sum + random.randint(-3, 3)
        row.append(last_v)

        data[i] = row
        s = sum(row)
        agg_sum.append(s)
        total_sum += s

    # 构建 value -> (row, index) 的映射
    for i in range(k):
        for cnt, v in enumerate(data[i]):
            position[v] = (i, cnt)

    # --------------------------
    # 下方为原逻辑，去掉 input，封装为 main
    # --------------------------
    trace = defaultdict()
    F = [False for _ in range(1 << k)]
    back = [0 for _ in range(1 << k)]
    res = [(0, 0) for _ in range(k)]

    def build_mask(trace_mask):
        if trace_mask == 0:
            return

        if trace.get(trace_mask):
            for d in trace.get(trace_mask):
                fr, to, v = d
                res[fr] = (v, to)
            return

        sub_mask = back[trace_mask]
        build_mask(sub_mask)
        build_mask(trace_mask - sub_mask)

    # 若总和不能整除 k，则一定无解
    if total_sum % k != 0:
        print("No")
        return

    target_row_sum = total_sum // k

    # 枚举每个起点
    for i in range(k):
        for cnt, value in enumerate(data.get(i), 0):
            x = i
            y = cnt
            mask = (1 << x)
            could = True
            circle = []
            while True:
                next_value = target_row_sum - agg_sum[x] + data.get(x)[y]
                if position.get(next_value) is None:
                    could = False
                    break

                last_x = x
                last_y = y

                x, y = position.get(next_value)
                circle.append((x, last_x, next_value))

                if x == i and y == cnt:
                    break

                if mask & (1 << x):
                    could = False
                    break

                mask |= (1 << x)

            F[mask] |= could
            if could:
                trace[mask] = circle

    # 子集 DP 合并若干个可行轮换
    for mask in range(1, 1 << k):
        sub = mask
        while sub > 0:
            if F[sub] and F[mask - sub]:
                F[mask] = True
                back[mask] = sub
                break
            sub = mask & (sub - 1)

    full_mask = (1 << k) - 1
    if F[full_mask]:
        print("Yes")
        build_mask(full_mask)
        for value, to in res:
            # 输出：取值 目标行号(1-based)
            print(value, to + 1)
    else:
        print("No")


if __name__ == "__main__":
    # 可以在这里调整规模 n（即原代码中的 k）
    main(4)