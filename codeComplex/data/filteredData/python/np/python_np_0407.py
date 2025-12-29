import random
from collections import defaultdict

def generate_test_data(n):
    """
    生成测试数据：
    - n: 行数（规模）
    返回: (n, m, matrix)
      n: 行数
      m: 列数
      matrix: n 行，每行一个长度为 m 的整数列表
    生成规则：
    - 设 m = min(20, max(1, n.bit_length())) 作为一个随规模变化的列数
    - 每个元素为 [0, 10] 的随机整数
    """
    m = min(20, max(1, n.bit_length()))
    matrix = [
        [random.randint(0, 10) for _ in range(m)]
        for _ in range(n)
    ]
    return n, m, matrix

def main(n):
    n, m, matrix = generate_test_data(n)

    elems = set()
    vals = defaultdict(list)

    # 收集所有出现过的值及其 (列位置, 行号)
    for i in range(n):
        for pos, v in enumerate(matrix[i]):
            elems.add(v)
            vals[v].append((pos, i))

    elems = sorted(elems, reverse=True)

    masks = [0] * n
    full = (1 << m) - 1
    met = {0: 0}

    for v in elems:
        for pos, i in vals[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # 输出行号（1-based）
                print(i + 1, met[complement] + 1)
                return

    # 如果没找到满足条件的两行，可以选择打印 -1 -1 或不输出
    # 这里选择不输出任何内容
    return

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)