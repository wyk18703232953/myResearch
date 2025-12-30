import random

def main(n):
    # 根据规模 n 生成测试数据，这里让 l 和 r 为 n 位内的随机整数，且 l <= r
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 原逻辑开始
    limit = l ^ r

    if limit != 0:
        limit = len(bin(limit)) - 2
        maxXor = '1' * limit
        result = int(maxXor, 2)
    else:
        result = 0

    print(result)

if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)