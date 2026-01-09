M = 10 ** 9 + 7

def solve(x, k):
    if x == 0:
        return 0
    P = pow(2, k, M)
    r = (P * x) % M - (0.5 * (-1 + P)) % M
    return int((2 * r + M) % M)

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设置 x = n, k = n，可按需调整生成策略
    x = n
    k = n
    ans = solve(x, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(10)