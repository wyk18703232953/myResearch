def main(n):
    # 生成确定性的 s，使其规模与 n 同阶
    s = n * (n + 1) // 2  # 任意确定性构造
    if n == 0:
        # print(0)
        pass
        return
    if s % n == 0:
        # print(s // n)
        pass

    else:
        # print(s // n + 1)
        pass
if __name__ == "__main__":
    main(10)