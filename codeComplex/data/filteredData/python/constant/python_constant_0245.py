def main(n):
    # 映射：将实验规模 n 映射到原程序的 n 和 m
    # 原 n = n
    # 原 m = 2 * n + 3（确定性构造）
    orig_n = n
    orig_m = 2 * n + 3

    r = 1
    for power in range(orig_n):
        r *= 2
        if r > orig_m:
            # print(orig_m)
            pass
            break

    else:
        if r == orig_m:
            # print(0)
            pass

        else:
            # print(orig_m % r)
            pass
if __name__ == "__main__":
    main(10)