from math import ceil

def main(n):
    # 令 k 与 n 成线性关系，确保规模可控且避免除以 0
    k = n + 1

    result = ceil((8 * n) / k) + ceil((5 * n) / k) + ceil((2 * n) / k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)