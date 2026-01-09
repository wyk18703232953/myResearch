def main(n):
    # 映射含义：
    # k: 固定为 3
    # n: 使用 main 的参数
    # s: 与 n 同阶，避免退化，例如 s = max(1, n//2)
    # p: 固定为 5
    k = 3
    s = max(1, n // 2)
    p = 5

    if (1 * n) % s == 0:
        need = (1 * n) // s
        if need == 0 and k % p == 0:
            result = k // p
        elif (k * need) % p == 0:
            result = (k * need) // p

        else:
            result = ((k * need) // p) + 1

    else:
        need = ((1 * n) // s) + 1
        if need == 0 and k % p == 0:
            result = k // p
        elif (k * need) % p == 0:
            result = (k * need) // p

        else:
            result = ((k * need) // p) + 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)