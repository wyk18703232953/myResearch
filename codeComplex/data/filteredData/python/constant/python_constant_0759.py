import math

def main(n):
    # 映射：原程序有两个输入 n, k
    # 这里将外部 n 映射为原 n，k 由一个确定性函数生成
    orig_n = n
    k = orig_n * (orig_n + 1) // 4

    a = (2 * orig_n + 3 - math.sqrt((2 * orig_n + 3) ** 2 - 4 * (orig_n ** 2 + orig_n - 2 * k))) // 2
    # print(int(a))
    pass
if __name__ == "__main__":
    main(10)