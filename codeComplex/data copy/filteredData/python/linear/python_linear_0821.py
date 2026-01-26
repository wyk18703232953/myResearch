def main(n):
    # 为了保持原程序的输入结构 (n, k)，这里将 k 作为 n 的函数确定性生成
    # 原输入：n, k = map(int, input().split())
    # 这里设定 k = n // 2，保证同一 n 下数据确定
    k = n // 2

    for p in range(n + 1):
        if p * (p + 1) // 2 - (n - p) == k:
            # 原程序在找到时打印 n-p，这里直接返回，便于实验复杂度
            return n - p

    # 若未找到解，可以返回一个固定值（例如 -1），以保持函数总是有返回值
    return -1


if __name__ == "__main__":
    # 示例调用，可按需要修改 n 的取值来做规模实验
    result = main(1000)
    # print(result)
    pass