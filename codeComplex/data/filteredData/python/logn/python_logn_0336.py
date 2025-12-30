import random

MOD = 1000000007

def binar(a, st, d):
    if st == 0:
        return 1
    elif st == 1:
        return a % d
    return (binar(a * a % d, st // 2, d) * binar(a, st % 2, d)) % d

def main(n):
    # 根据规模 n 生成测试数据：
    # 令 k 与 n 相关，x 在 [0, MOD-1] 范围内
    x = random.randint(0, MOD - 1)
    k = n

    if x == 0:
        print(0)
        return

    res = ((x * binar(2, k + 1, MOD)) - binar(2, k, MOD) + 1) % MOD
    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)