import sys

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

        for i in range(s + 1, n, 1):
            if stages[i] - stages[s] > 1:
                backtrack(i, w + stages[i], t + 1)

    backtrack(0, stages[0], 1)

    if min_weight == float('inf'):
        return -1

    return min_weight

def main(n):
    # 映射规则：
    # n >= 2 时：
    #   k = (n // 2) + 1，确保 1 <= k <= len(stages)
    #   stages 由前 m 个小写字母生成，其中 m = max(2, min(26, n))
    #   原程序中 stages 从字符串去重后排序，这里直接构造等价结果：严格递增的整数列表
    #
    # n <= 1 时，构造一个最小但合法的输入规模：
    #   使用 n_eff = 2 进行实验

    if n <= 1:
        n_eff = 2
    else:
        n_eff = n

    # stages 的规模
    m = max(2, min(26, n_eff))

    # 构造一个“字符串”对应的去重排序结果：
    # 用 'a', 'c', 'e', ... 的模式生成，转为 cint
    # 确保严格递增且间隔至少 1，从而为 backtrack 提供可行路径
    stages_chars = []
    for i in range(m):
        # 生成字母下标：0,2,4,...，再截断到 25（'z'）
        idx = (2 * i) % 26
        stages_chars.append(chr(ord('a') + idx))
    stages_int = sorted(set(cint(c) for c in stages_chars))
    stages = stages_int

    # 设置 k，1 <= k <= len(stages)
    k = (n_eff // 2) + 1
    if k < 1:
        k = 1
    if k > len(stages):
        k = len(stages)

    # n 参数在原函数中只用于长度，这里传入 len(stages)
    result = find_min_weight(len(stages), k, stages)
    # 为了符合原程序行为，这里返回结果；上层可选择打印或仅用于计时
    return result

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小做规模实验
    n = 10
    ans = main(n)
    print(ans)