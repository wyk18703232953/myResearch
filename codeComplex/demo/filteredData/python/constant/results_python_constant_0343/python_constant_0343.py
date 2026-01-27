def main(n):
    if n == 0:
        # print(0)
        pass
    elif n % 2 == 1:
        # print((n + 1) // 2)
        pass

    else:
        # print(n + 1)
        pass
if __name__ == "__main__":
    # 示例：对若干固定规模进行调用，便于做时间复杂度实验
    for size in range(0, 11):
        main(size)