from math import ceil

def main(n):
    # 映射：原程序有两个输入 n, k
    # 这里将第一个参数视为原来的 n，k 由 n 确定性生成
    orig_n = n
    k = n + 1 if n > 0 else 1  # 保证 k >= 1 且与 n 有确定关系

    result = ceil(orig_n * 2 / k) + ceil(orig_n * 5 / k) + ceil(orig_n * 8 / k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)