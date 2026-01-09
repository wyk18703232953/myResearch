import math

def main(n):
    # 对于原程序，输入有两个整数 n 和 k
    # 这里将实验规模参数 n 作为原始 n 的大小
    # 并构造一个确定性的 k，与 n 同阶，用于时间复杂度实验
    orig_n = n
    # 构造一个确定性的 k，保证与 n 有非平凡关系
    # 这里选择大约是序列和的一半：k ≈ n(n+1)/4
    k = (orig_n * (orig_n + 1)) // 4

    # 原始算法逻辑
    if (3 + 2 * orig_n + math.sqrt((3 + 2 * orig_n) ** 2 - 4 * (orig_n + orig_n ** 2 - 2 * k))) / 2 < orig_n:
        m1 = (3 + 2 * orig_n + math.sqrt((3 + 2 * orig_n) ** 2 - 4 * (orig_n + orig_n ** 2 - 2 * k))) / 2

    else:
        m1 = (3 + 2 * orig_n - math.sqrt((3 + 2 * orig_n) ** 2 - 4 * (orig_n + orig_n ** 2 - 2 * k))) / 2

    # print(int(m1))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小做时间复杂度实验
    main(10_000)