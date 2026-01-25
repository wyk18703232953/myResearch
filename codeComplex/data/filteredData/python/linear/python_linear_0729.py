def main(n):
    # 将原来的 k 设置为与 n 相关的确定性值，保证规模可控且 1 <= k <= n
    if n <= 0:
        return
    k = n // 2 if n > 1 else 1

    chuj_twojej_starej = (n - k) // 2 + 1
    i = 1
    while True:
        if i % chuj_twojej_starej == 0:
            print(0, end="")
        else:
            print(1, end="")
        if i == n:
            break
        i += 1


if __name__ == "__main__":
    main(10)