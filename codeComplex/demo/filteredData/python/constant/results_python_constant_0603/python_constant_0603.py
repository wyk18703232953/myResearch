from math import ceil

def main(n):
    # 映射：原程序中有两个输入 n 和 k
    # 这里将实验规模参数作为原始的 n
    # 并构造一个与 n 相关的、确定性的 k
    k = max(1, n // 2 + 1)

    cou = 0
    cou += ceil(n * 2 / k)
    cou += ceil(n * 5 / k)
    cou += ceil(n * 8 / k)
    # print(cou)
    pass
if __name__ == "__main__":
    main(10)