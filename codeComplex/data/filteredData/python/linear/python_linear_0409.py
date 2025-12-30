import random
import string

def cint(c):
    return ord(c) - 96

def find_min_weight(n, k, stages):
    n = len(stages)
    min_weight = float('inf')

    def backtrack(s, w, t):
        nonlocal min_weight

        if t >= k:
            min_weight = min(min_weight, w)
            return

        if s >= n - 1:
            return

        for i in range(s + 1, n):
            if stages[i] - stages[s] > 1:
                backtrack(i, w + stages[i], t + 1)

    if not stages:
        return -1

    backtrack(0, stages[0], 1)

    if min_weight == float('inf'):
        return -1

    return min_weight


def main(n):
    # 生成测试数据：
    # 1) 随机选择字符串长度 L（1 到 n）
    L = max(1, n)
    # 2) 生成含有小写字母的随机字符串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(L))
    # 3) 将字符串转为 stages，模拟原逻辑：去重、映射、排序
    stages = sorted(set(map(cint, s)))
    # 4) 规模参数 n 不再从外部读入，这里使用 len(stages) 传入
    #    生成 k（在 1 到 len(stages) 之间）
    if len(stages) == 0:
        return -1
    k = random.randint(1, len(stages))

    return find_min_weight(len(stages), k, stages)


# 示例：直接运行本文件时执行一次 main
if __name__ == "__main__":
    result = main(10)
    print(result)