def main(n):
    # 原程序逻辑：
    # from sys import stdin
    # n = int(stdin.readline()) + 1
    # if n == 1:
    #     print(0)
    # else:
    #     print(n//2 if n%2 == 0 else n)
    #
    # 这里将输入规模参数 n 对应为原始输入 x，使得：
    # x = n
    # 内部使用 n_internal = x + 1 = n + 1
    n_internal = n + 1
    if n_internal == 1:
        result = 0

    else:
        result = n_internal // 2 if n_internal % 2 == 0 else n_internal
    # print(result)
    pass
if __name__ == "__main__":
    main(10)