from math import sqrt

def main(n):
    # 根据 n 生成测试数据，这里示例：令 k = n 的一半
    k = n // 2

    val = int(sqrt(9 + 8 * (n + k)))
    ans = (-3 + val) // 2
    # print(n - ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)