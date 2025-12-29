def find(n, k):
    x = 9 + 8 * (n + k)
    a = (-3 + int(x ** 0.5)) // 2
    b = n - a
    return b

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 k = n，用于示例；可按需要修改生成策略
    k = n
    result = find(n, k)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需修改 n
    main(10)