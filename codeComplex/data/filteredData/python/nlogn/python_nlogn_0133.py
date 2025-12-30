import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # m: 目标值（设为 n 到 2n 之间）
    # k: 初始值（设为 0 到 m 之间）
    m = random.randint(max(1, n), max(1, 2 * n))
    k = random.randint(0, m)
    a = [random.randint(1, 10) for _ in range(n)]

    # 原程序逻辑
    a.sort(reverse=True)
    no = 0
    while k < m and no < n:
        k += a[no] - 1
        no += 1
    if k < m:
        print(-1)
    else:
        print(no)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)