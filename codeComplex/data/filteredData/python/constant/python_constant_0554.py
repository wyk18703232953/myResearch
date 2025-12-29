import random

def main(n: int):
    # 生成测试数据：
    # n: 给定的规模
    # 为了保证参数有意义，我们生成：
    # m ∈ [1, max(1, n)]
    # k, l ∈ [0, n]
    if n <= 0:
        return  # 规模无效时直接返回

    m = random.randint(1, max(1, n))
    k = random.randint(0, n)
    l = random.randint(0, n)

    need = k + l
    if need % m == 0 and need <= n:
        print(need // m)
    else:
        x = need // m + 1
        if x * m > n:
            print(-1)
        else:
            print(x)


if __name__ == "__main__":
    # 示例：以 n = 100 作为规模运行
    main(100)