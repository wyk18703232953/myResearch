import math

def main(n):
    # 将 n 映射到原程序的 k, n_items, s, p
    # 保证各值为正整数，并随 n 线性扩展，且完全确定
    k = max(1, n // 3)
    n_items = max(1, n)
    s = max(1, n // 2)
    p = max(1, n // 4)

    x = math.ceil(n_items / s)
    y = math.ceil(x * k / p)
    # print(y)
    pass
    return y

if __name__ == "__main__":
    main(100)