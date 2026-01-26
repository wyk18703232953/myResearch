def main(n):
    # 生成确定性的 k，保证 1 <= k <= 2n+2
    if n <= 0:
        # print(0)
        pass
        return
    k = 2 * n // 3 + 3

    if k > n * 2 or k < 3:
        # print(0)
        pass
    elif n >= k - 1:
        # print(k - k // 2 - 1)
        pass

    else:
        # print(n - k // 2)
        pass
if __name__ == "__main__":
    main(10)