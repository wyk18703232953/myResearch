def main(n):
    rang = list(range(2, n // 2 + 1))
    a = [i * (n // i - 1) for i in rang]
    result = sum(a) * 4
    return result

if __name__ == "__main__":
    # 示例：使用一个固定的规模 n 调用 main
    n = 1000
    ans = main(n)
    # print(ans)
    pass