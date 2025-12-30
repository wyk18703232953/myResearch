import random
from collections import defaultdict

def main(n):
    # 生成规模参数
    # n: 行数
    # m: 列数，这里设为 n 的一个函数；可按需要调整
    m = max(1, min(20, n))  # 控制 m 不至于太大

    # 生成测试数据：n 行，每行 m 个随机整数
    # 为保证有解，构造时可以随机生成；原逻辑依赖数据本身是否存在满足条件的两行
    a = [
        [random.randint(1, 10**9) for _ in range(m)]
        for _ in range(n)
    ]

    vals = set()
    locs = defaultdict(list)
    for i in range(n):
        for pos, v in enumerate(a[i]):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n
    full = (1 << m) - 1
    met = {0: 0}

    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # 输出满足条件的两行编号（从 1 开始）
                print(i + 1, met[complement] + 1)
                return

    # 若没有找到满足条件的两行，可选择输出特殊值或不输出
    # 这里什么都不做，函数结束即可


if __name__ == "__main__":
    # 示例：调用 main，规模 n=10
    main(10)