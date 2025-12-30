M = 10**9 + 7

def pw(x, y):
    r = 1
    x = x % M
    while y:
        if y & 1:
            r = (r * x) % M
        y >>= 1
        x = (x * x) % M
    return r

def main(n):
    # 依据规模 n 生成测试数据：
    # 这里约定：k = n，x = n（可按需调整生成规则）
    x = n
    k = n

    ans = pw(2, k + 1) * x - pw(2, k) + 1 + M
    if x == 0:
        ans = 0
    ans %= M

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)