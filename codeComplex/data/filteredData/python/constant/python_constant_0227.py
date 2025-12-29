import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 这里 n 只影响生成数据的范围，并不改变原算法规模
    # 例如令 a,b,x,y,z 在 [0, n] 范围内随机生成
    a = random.randint(0, n)
    b = random.randint(0, n)
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    # 原始逻辑
    yel = x * 2 + y
    bul = y + z * 3
    ans = max(0, yel - a) + max(0, bul - b)

    print(ans)


if __name__ == "__main__":
    # 示例：可在此调用 main，并设定规模 n
    main(10)