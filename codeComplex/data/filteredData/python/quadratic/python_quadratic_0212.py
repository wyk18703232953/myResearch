import random

def main(n):
    # 生成测试数据：n 个 m 位的二进制整数
    # 这里设置 m 与 n 相同，可按需要调整生成规则
    m = n
    # 生成 n 个随机 m 位二进制数，类型为 int
    a = []
    for _ in range(n):
        # 生成一个 [0, 2^m - 1] 之间的随机整数
        x = random.getrandbits(m)
        a.append(x)

    # 原始逻辑开始
    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x
    result = ("YES", "NO")[all(x & s & ~t for x in a)]

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)，可自行修改规模
    main(5)