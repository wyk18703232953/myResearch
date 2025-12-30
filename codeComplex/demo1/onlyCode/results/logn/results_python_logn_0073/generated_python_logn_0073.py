import random

def main(n: int):
    # 1. 根据规模 n 生成测试数据 l, r
    # 这里示例：生成 0 <= l, r < 2^n 的随机整数
    if n <= 0:
        l = 0
        r = 0
    else:
        upper = 1 << n
        l = random.randrange(0, upper)
        r = random.randrange(0, upper)

    # 2. 原始逻辑
    limit = l ^ r

    if limit != 0:
        limit = len(bin(limit)) - 2
        maxXor = '1' * limit
        ans = int(maxXor, 2)
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(5)