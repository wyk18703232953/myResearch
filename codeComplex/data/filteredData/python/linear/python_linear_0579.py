import random

def main(n):
    # 根据 n 生成测试数据：s 设为一个与 n 同规模量级的数
    # 这里设定 s 在 [n, 10*n] 区间内随机生成
    s = random.randint(n, 10 * n)

    res = 0
    for i in range(n, 0, -1):
        res += s // i
        s = s % i
    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)