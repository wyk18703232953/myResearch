from math import sqrt

def main(n):
    # 由于原程序有两个输入 n, k，这里将规模 n 解释为原程序中的 n，
    # 并以一个确定性的方式生成 k，例如 k = n * (n + 1) // 2
    k = n * (n + 1) // 2
    result = int(n - 0.5 * (sqrt(8 * (k + n) + 9) - 3))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)