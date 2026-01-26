def main(n):
    # 确定性生成 k，与 n 同规模数量级
    k = n // 2
    a = pow(1 + 2 * k + 2 * n, 0.5) - 1
    result = n - int(a)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)