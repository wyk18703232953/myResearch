def main(n):
    # 生成确定性的输入 l 和 r，使得：
    # l = 0
    # r = (2^n) - 1
    # 这样 l ^ r = (2^n) - 1，循环会将 x 提升到 2^n，输出为 (2^n) - 1
    if n <= 0:
        l = 0
        r = 0

    else:
        l = 0
        r = (1 << n) - 1

    p = l ^ r
    x = 1
    while x <= p:
        x = x << 1
    # print(x - 1)
    pass
if __name__ == "__main__":
    main(10)