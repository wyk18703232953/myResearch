import random

def main(n):
    # 生成测试数据：m 为随机的边数规模，这里设为 n 的 1~2 倍
    m = random.randint(n, 2 * n)

    # 随机生成 m 个 1..n 的整数，模拟原先从输入读取的一行数字
    c = [random.randint(1, n) for _ in range(m)]

    # 原逻辑开始
    aa = [0] * (n + 1)
    for cc in c:
        aa[cc] += 1
    result = min(aa[1:])
    print(result)
    return result

if __name__ == "__main__":
    # 示例：可以修改这里的 n 来跑不同规模
    main(10)