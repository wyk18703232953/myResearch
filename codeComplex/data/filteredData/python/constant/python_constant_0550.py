from math import ceil

def main(n):
    # 映射：n 作为原程序中的 n，k 设为与 n 有关的确定性值
    # 避免除零，保证 k >= 1
    k = n // 2 + 1
    result = ceil(n / k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)