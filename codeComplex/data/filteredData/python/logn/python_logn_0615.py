def candy_eaten(n, k):
    choco = 1
    last = 1
    eat = 0
    i = n - 1
    while i > 0:
        if choco > k:
            temp = choco - k
            choco -= temp
            eat += temp
            i -= temp

        else:
            last += 1
            choco += last
            i -= 1
    return eat


def main(n):
    # 将 n 作为问题规模：构造 (N, K)
    # 例如 N = n，K 为与 n 相关的确定性函数
    N = n
    if N < 1:
        N = 1
    K = max(1, N // 2)
    result = candy_eaten(N, K)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)