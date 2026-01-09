def binary(n, k):
    lower = 1
    upper = n
    while lower < upper:
        mid = (lower + upper) // 2
        total = (mid * (mid + 1)) // 2
        if n - mid == total - k:
            # print(n - mid)
            pass
            break

        else:
            if n - mid > total - k:
                lower = mid + 1

            else:
                upper = mid


def main(n):
    # 确定性生成 (n, k)
    # 保证 k 在一个与 n 规模相关且可控的范围内
    if n <= 0:
        return
    N = n
    K = (n * (n + 1) // 2) // 2  # 与 n 规模相关的确定性构造
    if N == 1 and K == 1:
        # print(0)
        pass

    else:
        binary(N, K)


if __name__ == "__main__":
    main(10)