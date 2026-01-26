def main(n):
    # 映射：n 作为右边界 r，左边界 l 固定为 0
    l = 0
    r = n

    pop = l ^ r
    result = 1

    while result <= pop:
        result = result << 1

    # print(result - 1)
    pass
if __name__ == "__main__":
    main(10)