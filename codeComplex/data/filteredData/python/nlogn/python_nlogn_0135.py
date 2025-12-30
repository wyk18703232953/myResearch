import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # m: 目标值，设为 n 到 2n 之间
    # k: 初始值，设为 0 到 m 之间
    m = random.randint(max(1, n), max(2, n * 2))
    k = random.randint(0, m)
    a = [random.randint(1, 10) for _ in range(n)]

    # 原逻辑
    a.sort()
    a = a[::-1]
    if m <= k:
        print(0)
        return
    else:
        c = 0
        while c < n:
            k = k + a[c] - 1
            c += 1
            if k >= m:
                print(c)
                return
        else:
            print(-1)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)