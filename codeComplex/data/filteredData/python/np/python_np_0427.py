from collections import defaultdict
import random

def main(n):
    # 参数说明：
    # n: 行数（原程序中的 n）
    # m: 列数（原程序中的 m），这里可根据需要设置或随 n 调整
    m = max(1, min(20, n))  # 示例：m 不宜太大，否则位掩码过大

    # 生成测试数据：n 行，每行 m 个整数
    # 为了有更大概率存在答案，将值随机生成在一个较小范围内
    # 但不保证一定有解，行为与原程序一致：找不到就无输出
    vals = set()
    locs = defaultdict(list)
    a = [[random.randint(1, 10 * n) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for pos, v in enumerate(a[i]):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n
    full = (1 << m) - 1
    met = {0: 0}

    # 原逻辑：按值从大到小遍历
    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # 找到一对满足掩码互补的行，输出行号（1-based）
                print(i + 1, met[complement] + 1)
                return

if __name__ == "__main__":
    # 示例调用
    main(10)