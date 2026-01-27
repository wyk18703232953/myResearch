def main(n):
    # 在原程序中，n 和 s 都来自输入：n, s = list(map(int, input().split()))
    # 这里我们用 n 作为规模参数，确定性地构造 s
    if n <= 0:
        return 0
    s = n * (n + 1) // 2
    num_1 = s // n
    if s % n == 0:
        result = num_1

    else:
        result = num_1 + 1
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)