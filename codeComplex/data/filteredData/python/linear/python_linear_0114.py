from math import ceil

def main(n: int) -> int:
    # 生成规模为 n 的测试数据，这里原代码仅需一个整数 N
    N = n

    S = (N * (N + 1)) / 2
    F = int(ceil(N / 2.0))
    ans = int((S + F) / 2)

    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # 示例：使用 n = 10 作为测试
    main(10)