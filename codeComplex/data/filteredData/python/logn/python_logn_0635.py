from collections import defaultdict

def main(n):
    """
    依据规模 n 生成测试数据并执行原逻辑。
    原逻辑：给定 n, k，寻找最小的 cand 使得在累加序列中满足条件，
    输出 tot - k。
    这里根据 n 自动生成 k（可按需要调整生成策略）。
    """
    # 生成测试数据：n 为给定规模，k 取一个与 n 相关的值
    # 例如：k = n * (n + 1) // 4（约为前 n 项和的一半）
    if n <= 0:
        return 0  # 边界情况：n 非正时，直接返回 0

    k = n * (n + 1) // 4

    cand = 0
    tot = 0
    p = 0
    # 原条件：while tot < k or tot - (n - p) != k:
    while tot < k or tot - (n - p) != k:
        cand += 1
        tot += cand
        p += 1

    result = tot - k
    # 这里选择返回结果而不是打印，方便在其他环境中调用
    return result


if __name__ == '__main__':
    # 示例：自行设定一个 n，用于本地测试
    test_n = 10
    print(main(test_n))