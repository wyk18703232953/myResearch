def main(n):
    # 原程序逻辑：
    # a = input()
    # b = int(a) + 1
    # if b == 1: print("0")
    # elif b % 2 == 0: print(b // 2)
    # else: print(b)
    #
    # 这里将“输入规模” n 映射为原来的单个整数输入 a。
    # 为保证可规模化且确定，直接令 a = n。
    a = n
    b = a + 1
    if b == 1:
        result = 0
    elif b % 2 == 0:
        result = b // 2

    else:
        result = b
    return result


if __name__ == "__main__":
    # 示例：用若干不同规模运行，便于做时间复杂度实验时扩展
    for n in [0, 1, 2, 5, 10]:
        # print(f"n={n}, result={main(n)}")
        pass