def main(n):
    # 根据 n 生成确定性的 l 和 r
    l = n
    r = 2 * n + 3
    x = l ^ r
    pow_val = 1
    while pow_val <= x:
        pow_val *= 2
    # print(pow_val - 1)
    pass
if __name__ == "__main__":
    main(10)