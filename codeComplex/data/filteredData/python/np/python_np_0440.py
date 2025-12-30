import random
from collections import defaultdict


def main(n):
    # 1. 生成测试数据
    # 这里按原程序含义构造数据：
    # - 有 n 行
    # - 每行有 m 个整数
    # - 值相同的列模式用于触发算法逻辑
    #
    # 由于原代码依赖 m（每行元素个数），
    # 这里选择 m = max(1, n.bit_length()) 作为一个随规模增长的列数定义，
    # 也可以根据需要修改为常数或其他函数。
    m = max(1, n.bit_length())

    # 生成矩阵 data：n 行，每行 m 个整数
    # 为方便观察和触发逻辑，构造一些重复值模式，再填充随机数
    data = []
    for i in range(n):
        row = []
        for j in range(m):
            # 简单构造：值和行、列有关系，保证有重复的值出现
            # 例如：v = (i + j) % (m // 2 + 1)
            v = (i + j) % max(1, m // 2 + 1)
            row.append(v)
        data.append(row)

    # 2. 原逻辑封装（用生成好的 data 替代 input()）
    vals = set()
    locs = defaultdict(list)

    for i in range(n):
        for pos, v in enumerate(data[i]):
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
                # 输出与原程序一致：1-based 下标
                print(i + 1, met[complement] + 1)
                return

    # 若未找到匹配对（理论上可能），可选地输出提示或保持沉默
    # 这里保持沉默，以贴近原逻辑（原程序直接退出）。


if __name__ == "__main__":
    # 示例：调用 main(n)，可以根据需要修改 n
    main(10)