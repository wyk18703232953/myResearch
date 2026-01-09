mod = int(1e9 + 7)

def main(n):
    # 根据 n 生成测试数据：这里令 k = n（可按需修改生成策略）
    k = n

    if n > 0:
        ans = pow(2, k + 1, mod) * n - pow(2, k, mod) + 1

    else:
        ans = 0

    # print(ans % mod)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或在外部调用 main(n)
    main(10)