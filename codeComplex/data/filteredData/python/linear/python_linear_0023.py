import random

def main(n):
    # 生成规模为 n 的测试数据：随机整数列表
    # 使用随机数范围较大以避免过多重复，但结果只看奇偶性
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 对每个数取模 2，得到 0/1 列表（偶数为0，奇数为1）
    l = [x % 2 for x in arr]

    # 如果恰好有一个奇数，则输出该元素的位置(1-based)，否则抛出异常与原逻辑一致
    print(l.index(sum(l) == 1) + 1)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)