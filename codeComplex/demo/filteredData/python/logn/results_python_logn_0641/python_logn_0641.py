def sportMafia(n, k):
    import math
    r = round(n + 1.5 - math.sqrt(2 * (n + k) + 2.75))
    return r

def main(n):
    # 将 n 作为原问题中的 n
    # 构造确定性的 k，使规模随 n 线性变化
    k = n * (n // 2)
    result = sportMafia(n, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)