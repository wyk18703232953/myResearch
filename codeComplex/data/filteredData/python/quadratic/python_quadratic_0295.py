def main(n: int) -> int:
    """
    原逻辑封装为函数:
    - n 为规模，表示将生成长度为 2*n 的数组 a（保证成对结构，可包含不相邻相同元素）。
    - 返回原程序中最终的 z 值。
    这里生成的测试数据策略：
    - 构造一个包含 n 个“配对”的数组，每个数出现两次。
    - 然后打乱这些元素，以制造不相邻的相同元素，便于测试原逻辑。
    """
    import random

    # 生成测试数据：2*n 个元素，每个整数出现两次
    base = list(range(1, n + 1))
    a = base + base  # [1,2,...,n,1,2,...,n]
    random.shuffle(a)

    # 原始逻辑开始（去掉 input，使用生成的 a）
    length = 2 * n
    z = 0
    i = 0
    # 每次看一对 (a[i], a[i+1])，步长为 2
    while i < length - 1:
        if a[i] != a[i + 1]:
            # 找到后面第一个与 a[i] 相等的元素
            for j in range(i + 1, length):
                if a[j] == a[i]:
                    z += j - i - 1
                    # 将该元素移动到 i+1 位置
                    val = a.pop(j)
                    a.insert(i + 1, val)
                    break
        i += 2
    return z