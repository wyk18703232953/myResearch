M = 10**9 + 7

def power(x, y):
    if y == 0:
        return 1
    z = (power(x, y // 2) ** 2) % M
    if y % 2:
        z = (z * x) % M
    return z % M

def main(n):
    # 根据规模 n 生成测试数据，这里令 k = n（可按需要调整生成方案）
    k = n

    if n != 0:
        z = (((2 * n - 1 + M) % M) * power(2, k) + 1) % M

    else:
        z = 0
    # print(z)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)