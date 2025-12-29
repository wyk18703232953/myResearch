m = 1000000007

def power(x, y, p=1000000007):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

def main(n):
    # 根据规模 n 生成测试数据 (x, k)
    # 这里示例使用简单的生成策略：
    # x 在 [0, n] 内，k 在 [0, n] 内
    # 可按需自行修改生成逻辑
    x = n % m
    k = n

    if x == 0:
        print(0)
    elif k == 0:
        print((x * 2) % m)
    else:
        temp = power(2, k)
        maxi = (((x * temp) % m) * 2) % m
        mini = (m + maxi - (2 * (temp - 1)) % m) % m
        print((((maxi + mini) % m) * 500000004) % m)

if __name__ == "__main__":
    # 示例：调用 main，规模 n = 10
    main(10)