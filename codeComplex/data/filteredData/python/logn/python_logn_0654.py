import random

def main(n):
    # 生成测试数据：随机选择 i，使得等式有解
    # 方程：(i*(i+1))//2 - (n - i) = k  =>  k = (i*(i+1))//2 - (n - i)
    # 按原程序 i 范围 [1, 1000000]
    i_test = random.randint(1, 1_000_000)
    k = (i_test * (i_test + 1)) // 2 - (n - i_test)

    ans = 0
    for i in range(1, 1_000_001):
        val = (i * (i + 1)) // 2
        if val - (n - i) == k:
            ans = n - i
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调节
    main(10**6)