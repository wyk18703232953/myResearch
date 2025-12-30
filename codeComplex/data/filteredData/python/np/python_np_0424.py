import random
from collections import defaultdict

def main(n):
    # 1. 生成测试数据
    # 设定列数 m，可以根据需要调整为其他规则
    m = max(1, min(20, n))  # 简单设定：m 不大于 20，且至少为 1

    # 生成一个 n 行、m 列的整数矩阵 data
    # 数值范围设为 0~9（可根据需要调整）
    data = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

    # 2. 原逻辑实现（使用 data 替代 stdin）
    vals = set()
    locs = defaultdict(list)

    # 收集所有值及其位置
    for i in range(n):
        for pos, v in enumerate(data[i]):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n
    full = (1 << m) - 1
    met = {0: 0}

    # 按值从大到小遍历
    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # 输出两行的编号（1-based）
                print(i + 1, met[complement] + 1)
                return

    # 若逻辑没有找到匹配的两行，可以选择输出一些信息或保持沉默
    # 这里选择无输出（可按需求修改）
    return

if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)