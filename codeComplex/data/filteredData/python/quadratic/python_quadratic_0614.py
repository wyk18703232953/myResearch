import random

def main(n):
    # 生成测试数据：m 为 1..n 之间的随机数，k 为 1..10 的随机数，a 为 1..10 之间的随机整数数组
    if n <= 0:
        return 0

    m = random.randint(1, n)
    k = random.randint(1, 10)
    a = [random.randint(1, 10) for _ in range(n)]

    ret = 0
    for i in range(m):
        cur = 0
        for j in range(i, n):
            if j % m == i:
                cur = max(0, cur)
                cur -= k
            cur += a[j]
            ret = max(ret, cur)
    print(ret)
    return ret

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)